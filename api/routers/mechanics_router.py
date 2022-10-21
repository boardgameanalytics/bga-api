from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Mechanics Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/mechanics")
async def read_mechanics(body: SummaryQuery):
    """List game mechanics and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="mechanic",
                                   order_by=body.order_by,
                                   ascending=body.ascending,
                                   limit=body.limit)


@Router.post("/mechanics/{mechanic}")
async def read_mechanic_games(mechanic: str, body: GamesQuery):
    """List games with specific mechanic"""
    return Router.db.group_games(group_type="mechanic",
                                 group_name=mechanic,
                                 order_by=body.order_by,
                                 ascending=body.ascending,
                                 limit=body.limit)
