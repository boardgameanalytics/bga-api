from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Categories Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/categories")
async def read_categories(body: SummaryQuery):
    """List game categories and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="category",
                                   order_by=body.order_by,
                                   ascending=body.ascending,
                                   limit=body.limit)


@Router.post("/categories/{category}")
async def read_category_games(category: str, body: GamesQuery):
    """List games with specific category"""
    return Router.db.group_games(group_type="categories",
                                 group_name=category,
                                 order_by=body.order_by,
                                 ascending=body.ascending,
                                 limit=body.limit)
