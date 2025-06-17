from fastapi import HTTPException, status
from config.dbConfig import supabase

async def logout_user():
    try:
        supabase.auth.sign_out()
        return {"message":"logout successfully"}
    
    except Exception as e:
        print(f"logout error:{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="internal server error during logout"
        )
        
        
async def refresh_token():
    try:
       auth_response= supabase.auth.refresh_session()
       if not auth_response.session:
           raise HTTPException(
               status_code=status.HTTP_401_UNAUTHORIZED,
               detail="Invalid or expired refresh token"
           )
       return {
            "message": "Token refreshed successfully",
            "access_token": auth_response.session.access_token,
            "refresh_token": auth_response.session.refresh_token,
            "expires_in": auth_response.session.expires_in
        }
        
     
    except Exception as e:
        print(f"error while refrshing token:{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="internal server error during logout"
        )