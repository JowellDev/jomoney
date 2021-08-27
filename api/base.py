from fastapi import APIRouter
from api.endpoints import user_routes, transaction_routes

api_router = APIRouter()

api_router.include_router(user_routes.router, prefix='/users', tags=['users'])
api_router.include_router(transaction_routes.router, prefix='/transactions', tags=['transactions'])


