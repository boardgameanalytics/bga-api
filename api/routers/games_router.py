from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import GamesQuery

Router = APIRouter(
    tags=["Games Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/games")
async def read_games(params: GamesQuery = Depends()):
    """List basic game data"""
    return Router.db.read_games(
        order_by=params.order_by,
        ascending=params.ascending,
        limit=params.limit
    )


@Router.get("/games/{page}")
async def read_games(page: int, params: GamesQuery = Depends()):
    """List basic game data"""
    return Router.db.read_games(
        order_by=params.order_by,
        ascending=params.ascending,
        limit=params.limit
    )