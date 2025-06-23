from fastapi import APIRouter, HTTPException, status
from config.dbConfig import supabase

router = APIRouter()

@router.get("/all_users")
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
        import traceback, logging
        logging.error("get_users_and_members failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while fetching users and members."
        ) from exc





@router.get("/all_users/{id}")
async def get_user_by_id(id: str):
    """
    Return a single stakeholder by ID if role is 'user' or 'member'.
    """
    try:
        resp = supabase.table("Stakeholders").select("*").eq("user_id", id).in_("role", ["user", "member"]).execute()

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
