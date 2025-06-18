from fastapi import APIRouter
from models.stakeholders import LoginPayload, StakeholderSignup
from controllers.auth.signupController import signup_user
from controllers.auth.loginController import login_user

router = APIRouter()

@router.post("/signup", tags=["Auth"])
async def signup_route(payload:StakeholderSignup):
    return await signup_user(payload)

@router.post("/signin", tags=["Auth"])
async def signin_route(payload:LoginPayload):
    return await login_user(payload)