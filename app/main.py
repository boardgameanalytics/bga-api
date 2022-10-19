from fastapi import FastAPI

from app.data import DataBase
from app.routers import graph_router, rankings_router

API = FastAPI(
    title='BoardGameAnalytics REST API',
    version="0.0.1",
    docs_url='/',
)

API.db = DataBase()


@API.get("/version")
async def version():
    """API version and password
    <pre><code>
    @return: JSON[JSON[String,String]]</pre></code>"""
    return {"result": {"Version": API.version}}


for router in (graph_router, rankings_router):
    API.include_router(router.Router)
