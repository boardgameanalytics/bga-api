from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Designers Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/designers")
async def read_designers(params: SummaryQuery = Depends()):
    """List game designers and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="category",
                                   order_by=params.order_by,
                                   ascending=params.ascending,
                                   limit=params.limit)


@Router.get("/designers/{designer}")
async def read_category_games(designer: str, params: GamesQuery = Depends()):
    """List games by specific designer"""
    return Router.db.group_games(group_type="designers",
                                 group_name=designer,
                                 order_by=params.order_by,
                                 ascending=params.ascending,
                                 limit=params.limit)
