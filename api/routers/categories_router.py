from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Categories Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/categories")
async def read_categories(params: SummaryQuery = Depends()):
    """List game categories and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="category",
                                   order_by=params.order_by,
                                   ascending=params.ascending,
                                   limit=params.limit)


@Router.get("/categories/{category_id}")
async def read_category_games(category_id: int, params: GamesQuery = Depends()):
    """List games with specific category"""
    return Router.db.group_games(item_type="category",
                                 item_id=category_id,
                                 order_by=params.order_by,
                                 ascending=params.ascending,
                                 limit=params.limit)
