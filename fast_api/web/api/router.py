from fastapi.routing import APIRouter

from fast_api.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
