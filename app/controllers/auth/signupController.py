from fastapi import HTTPException, status
from models.stakeholders import StakeholderSignup
from config.dbConfig import supabase
import traceback

async def signup_user(payload: StakeholderSignup):
    try:
        #check if email already exists
        email_check_result = supabase.rpc('is_email_exist', {'email': payload.email}).execute()
        
        if email_check_result.data:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        

        # Supabase Auth with additional metadata
        auth_response = supabase.auth.sign_up({
            "email": payload.email,
            "password": payload.password,
            "options": {
                "data": {
                    "username": payload.username,
                    "role": payload.role or "user" #optional default user
                }
            }
        })

        user = auth_response.user
        
        if not user:
            raise HTTPException(status_code=400, detail="User signup failed - no user returned")

        print(f"Auth signup successful for user: {user.id}")
        
        response = {
                "message": "Signup successful",
                "user_id": user.id,
                "email": payload.email,
                "username": payload.username,
                "role": payload.role or "user", 
                "email_confirmation_required": True
            }
            
        print("User signup successfully")
        return response  

    except HTTPException:
       
        raise
    except Exception as e:
        print("Unexpected error:", traceback.format_exc())
        if hasattr(e, 'message'):
            raise HTTPException(status_code=400, detail=f"Signup failed: {e.message}")
        else:
            raise HTTPException(status_code=500, detail="Internal server error during signup")