from fastapi import APIRouter, HTTPException, status
from config.dbConfig import supabase

router = APIRouter()

@router.get("/users_and_members")
async def all_users():
    """
    Return all stakeholders where role is 'user' OR 'member'.
    """
    try:
        resp = supabase.table("Stakeholders").select("*").in_("role", ["user", "member"]).execute()
        
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
