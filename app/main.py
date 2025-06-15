from fastapi import FastAPI
import uvicorn
from config.config import settings
from config.dbConfig import supabase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "smartacademy chatbot"}

@app.on_event("startup")
async def check_supabase_connection():
    try:
       supabase.auth.sign_in_with_password({
            "email": "invalid@example.com",
            "password": "wrongpassword"
        })
       print("Failed to connect")
    except Exception as e:
        print(f"Connected to Supabase: {e}")
        
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )