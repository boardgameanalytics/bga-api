from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Publishers Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/publishers")
async def read_publishers(body: SummaryQuery):
    """List game publishers and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="publisher",
                                   order_by=body.order_by,
                                   ascending=body.ascending,
                                   limit=body.limit)


@Router.post("/publishers/{publisher}")
async def read_publisher_games(publisher: str, body: GamesQuery):
    """List games by specific publisher"""
    return Router.db.group_games(group_type="publisher",
                                 group_name=publisher,
                                 order_by=body.order_by,
                                 ascending=body.ascending,
                                 limit=body.limit)
