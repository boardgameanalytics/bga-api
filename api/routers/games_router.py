from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import GamesQuery

Router = APIRouter(
    tags=["Games Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/games")
async def read_games(body: GamesQuery):
    """List basic game data"""
    return Router.db.read_games(
        order_by=body.order_by,
        ascending=body.ascending,
        limit=body.limit
    )
