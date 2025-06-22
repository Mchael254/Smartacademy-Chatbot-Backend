from fastapi import APIRouter
from models.stakeholders import LoginPayload, StakeholderSignup
from controllers.api.usersController import all_users

router = APIRouter()

@router.get("/users")
async def all_user():
    return await all_users()


# update
# CREATE POLICY "Enable users to view their own data only"
# ON "public"."Stakeholders"
# FOR SELECT
# TO authenticated
# USING (
#   auth.uid() = user_id
# );
