from fastapi import FastAPI
from app.routers import contact
from app.config import settings

app = FastAPI(
    title= "Contact API",
    description= "well structured contact api",
    version= "1.0.0"
)

app.include_router(contact.router)

@app.get("/")
def root():
    return {"app": "Contacts API", "docs": "/docs"}
