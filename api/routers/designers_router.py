from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Designers Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/designers")
async def read_designers(body: SummaryQuery):
    """List game designers and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="category",
                                   order_by=body.order_by,
                                   ascending=body.ascending,
                                   limit=body.limit)


@Router.post("/designers/{designer}")
async def read_category_games(designer: str, body: GamesQuery):
    """List games by specific designer"""
    return Router.db.group_games(group_type="designers",
                                 group_name=designer,
                                 order_by=body.order_by,
                                 ascending=body.ascending,
                                 limit=body.limit)
