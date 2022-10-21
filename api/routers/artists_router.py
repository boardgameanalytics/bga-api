from fastapi import APIRouter, Depends

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Artists Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/artists")
async def read_artists(params: SummaryQuery = Depends()):
    """List game artists and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="artist",
                                   order_by=params.order_by,
                                   ascending=params.ascending,
                                   limit=params.limit)


@Router.get("/artists/{artist_id}")
async def read_artist_games(artist_id: int, params: GamesQuery = Depends()):
    """List games by specific artist"""
    return Router.db.group_games(item_type="artist",
                                 item_id=artist_id,
                                 order_by=params.order_by,
                                 ascending=params.ascending,
                                 limit=params.limit)
