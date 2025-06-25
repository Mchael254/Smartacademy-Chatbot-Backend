from fastapi import APIRouter, HTTPException, status
from config.dbConfig import supabase
import logging
import traceback


async def all_users():
    """
    Return all stakeholders where role is 'user' OR 'member'.
    """
    try:
        resp = supabase.table("Stakeholders").select("*").in_("role", ["user", "member"]).execute()
        print(resp)
        
        if not resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No users or members found."
            )
        return resp.data

    except Exception as exc:
        logging.error("get_users_and_members failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while fetching users and members."
        ) from exc


async def get_user_by_id(id: str):
    """
    Return a single stakeholder by ID if role is 'user' or 'member'.
    """
    try:
        resp = supabase.table("Stakeholders").select("email,username").eq("user_id", id).in_("role", ["user", "member"]).execute()

        if not resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User/member with id '{id}' not found."
            )

        return resp.data[0]  
    except Exception as exc:
        import traceback, logging
        logging.error("get_user_by_id failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while fetching the stakeholder."
        ) from exc
    
    
async def delete_user_by_id(id: str):
    try:
        # Step 1: Check if user exists with valid role
        resp = supabase.table("Stakeholders").select("user_id").eq("user_id", id).in_("role", ["user", "member"]).execute()

        if not resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User/member with id '{id}' not found."
            )

        # Step 2: Proceed with deletion
        delete_resp = supabase.table("Stakeholders").delete().eq("user_id", id).execute()

        # Step 3: Check if anything was deleted
        if not delete_resp.data:
            raise HTTPException(status_code=500, detail="Delete failed or no data returned from Supabase.")

        return {"message": f"User/member with id '{id}' successfully deleted."}

    except Exception:
        import traceback
        logging.error("delete_user_by_id failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while deleting the stakeholder."
        )
