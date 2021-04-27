from fastapi import APIRouter
from api_v1 import diecuts_routs, zub_routs, design_routs, digital_job_routs, customer_routs
from user import user_routs
from tags_docs import tags
routes = APIRouter()

routes.include_router(diecuts_routs.router, prefix="/api/v1/diecuts", tags=[tags[1]])
routes.include_router(zub_routs.router, prefix="/api/v1/zub", tags=[tags[2]])
routes.include_router(design_routs.router, prefix="/api/v1/design", tags=[tags[3]])
routes.include_router(digital_job_routs.router, prefix="/api/v1/djob", tags=[tags[4]])
routes.include_router(customer_routs.router, prefix="/api/v1/customer", tags=[tags[5]])
routes.include_router(user_routs.router, prefix="/api/v1/user", tags=[tags[6]])

