from fastapi import APIRouter
from models.stakeholders import LoginPayload, StakeholderSignup
from controllers.users.usersController import all_users,get_user_by_id,delete_user_by_id

router = APIRouter()

@router.get("/get_all_users", tags=["Users"])
async def all_user():
    return await all_users()

@router.get("/get_user/{id}", tags=["Users"])
async def get_by_id(id:str):
    return await get_user_by_id(id)

@router.delete("/delete_user/{id}", tags=["Users"])
async def delete_by_id(id:str):
    return await delete_user_by_id(id)

# update
# CREATE POLICY "Enable users to view their own data only"
# ON "public"."Stakeholders"
# FOR SELECT
# TO authenticated
# USING (
#   auth.uid() = user_id
# );
