from fastapi import FastAPI

from api.data import BoardgamesDB
from api.routers import artists_router, categories_router, designers_router, games_router, \
    mechanics_router, publishers_router

API = FastAPI(
    title='BoardGameAnalytics REST API',
    version="0.0.2",
    docs_url='/',
)

API.db = BoardgamesDB()


@API.get("/version")
async def version():
    """API version"""
    return {"result": {"Version": API.version}}


for router in (artists_router, categories_router, designers_router, games_router, mechanics_router, publishers_router):
    API.include_router(router.Router)
