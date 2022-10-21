from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import SummaryQuery, GamesQuery

Router = APIRouter(
    tags=["Artists Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/artists")
async def read_artists(body: SummaryQuery):
    """List game artists and aggregate statistics of matching games"""
    return Router.db.group_summary(group_type="artist",
                                   order_by=body.order_by,
                                   ascending=body.ascending,
                                   limit=body.limit)


@Router.post("/artists/{artist}")
async def read_artist_games(artist: str, body: GamesQuery):
    """List games by specific artist"""
    return Router.db.group_games(group_type="artist",
                                 group_name=artist,
                                 order_by=body.order_by,
                                 ascending=body.ascending,
                                 limit=body.limit)
