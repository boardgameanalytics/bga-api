from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Mechanics Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/mechanics")
async def read_mechanics(params: SummaryQuery = Depends()):
    """List game mechanics and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="mechanic",
                                   order_by=params.order_by,
                                   ascending=params.ascending,
                                   limit=params.limit)


@Router.get("/mechanics/{mechanic_id}")
async def read_mechanic_games(mechanic_id: int, params: GamesQuery = Depends()):
    """List games with specific mechanic"""
    return Router.db.group_games(item_type="mechanic",
                                 item_id=mechanic_id,
                                 order_by=params.order_by,
                                 ascending=params.ascending,
                                 limit=params.limit)
