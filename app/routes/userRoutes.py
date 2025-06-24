from fastapi import APIRouter
from models.stakeholders import LoginPayload, StakeholderSignup
from controllers.api.usersController import all_users,get_user_by_id,delete_user_by_id

router = APIRouter()

@router.get("/users")
async def all_user():
    return await all_users()


# http://localhost:8000/api/users/5456ae17-64d9-4004-8aba-62a8b8002343, kindly use the following api to test it
@router.get("/users/{id}")
async def get_by_id(id:str):
    return await get_user_by_id(id)

@router.delete("/users/{id}")
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
