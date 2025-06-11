from fastapi import FastAPI
import uvicorn
from config.config import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "smartacademy chatbot"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True  
    )