from fastapi import FastAPI
from app.services.mongo_service import get_document
from app.api.routes import router
from app.services.mongo_service import get_document
app = FastAPI(
    title="Summary Improvement Agent",
    version="1.0.0"
)

app.include_router(router)

# @app.get("/user/{user_id}")
# def get_user(user_id: str):
#     user = get_document("users", {"user_id": user_id})
#     return user
# def decrypt(encrypted_text):
#     # code here
#     pass