from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

import uvicorn
from config.config import settings
from config.dbConfig import supabase
from routes import authRoutes, userRoutes,modelRoutes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "smartacademy chatbot"}


# routes
app.include_router(authRoutes.router, prefix="/auth")
app.include_router(userRoutes.router, prefix="/api")
app.include_router(modelRoutes.router, prefix="/model")


@app.on_event("startup")
async def check_supabase_connection():
    try:
        supabase.auth.sign_in_with_password(
            {"email": "invalid@example.com", "password": "wrongpassword"}
        )
        print("Failed to connect")
    except Exception as e:
        print(f"Connected to Supabase: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=True)
