from fastapi import FastAPI

from api.data import BoardgamesDB
from api.routers import graph_router, games_router, groups_router

API = FastAPI(
    title='BoardGameAnalytics REST API',
    version="0.0.1",
    docs_url='/',
)

API.db = BoardgamesDB()


@API.get("/version")
async def version():
    """API version and password
    <pre><code>
    @return: JSON[JSON[String,String]]</pre></code>"""
    return {"result": {"Version": API.version}}


for router in (games_router, graph_router, groups_router):
    API.include_router(router.Router)
