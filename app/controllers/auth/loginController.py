from fastapi import HTTPException, status
from config.dbConfig import supabase
from models.stakeholders import LoginPayload, LoginResponse


async def login_user(payload:LoginPayload):
    try:
        #signin with supabase auth
        auth_response = supabase.auth.sign_in_with_password({
            "email":payload.email,
            "password":payload.password
        })
        
        if not auth_response.user or not auth_response.session:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        user_data = {
            "id": auth_response.user.id,
            "email": auth_response.user.email,
            "username": auth_response.user.user_metadata.get("username", ""),
            "role": auth_response.user.user_metadata.get("role", "user"),
            "email_confirmed": auth_response.user.email_confirmed_at is not None,
            "created_at": auth_response.user.created_at
        }
        
        return LoginResponse(
            message="Login successful",
            access_token=auth_response.session.access_token,
            refresh_token=auth_response.session.refresh_token,
            user=user_data,
            expires_in=auth_response.session.expires_in
        )
        
    
    except Exception as e:
        print(f"Login error: {str(e)}")
        
        # Supabase auth errors
        error_message = str(e).lower()
        if any(phrase in error_message for phrase in ["invalid", "wrong", "incorrect", "credentials"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        # elif "email not confirmed" in error_message:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Please confirm your email address before logging in"
        #     )
        elif "too many requests" in error_message:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many login attempts. Please try again later"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error during login"
            )