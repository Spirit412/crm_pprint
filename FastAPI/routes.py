from fastapi import APIRouter
from api_v1 import diecuts_routs, zub_routs

routes = APIRouter()

routes.include_router(diecuts_routs.router, prefix="/api/v1/diecuts")
routes.include_router(zub_routs.router, prefix="/api/v1/zub")

