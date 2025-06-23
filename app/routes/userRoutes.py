from fastapi import APIRouter
from controllers.users.usersController import all_users


router = APIRouter()

@router.get("/allUsers", tags=["Users"])
async def all_user():
    return await all_users()


