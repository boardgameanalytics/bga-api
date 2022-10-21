from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Publishers Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/publishers")
async def read_publishers(params: SummaryQuery = Depends()):
    """List game publishers and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="publisher",
                                   order_by=params.order_by,
                                   ascending=params.ascending,
                                   limit=params.limit)


@Router.get("/publishers/{publisher_id}")
async def read_publisher_games(publisher_id: int, params: GamesQuery = Depends()):
    """List games by specific publisher"""
    return Router.db.group_games(item_type="publisher",
                                 item_id=publisher_id,
                                 order_by=params.order_by,
                                 ascending=params.ascending,
                                 limit=params.limit)
