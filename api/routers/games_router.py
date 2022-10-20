from typing import Literal

from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import GameQuery

Router = APIRouter(
    tags=["Games Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/read/games")
async def read_games(query: GameQuery):
    """List basic game data
    <pre><code>
    @param query: GameQuery
    @return List[Game]</pre></code>"""
    return Router.db.read_games(query_obj=query)


@Router.get("/top/games/{order_by}")
async def read_all_games(
        order_by: Literal['bayes_rating', 'total_ratings', 'weight', 'popularity']
):
    """List basic game data
    <pre><code>
    @return List[Game]</pre></code>"""
    query = GameQuery(
        order_by=order_by,
        ascending=False,
        limit=10
    )
    return Router.db.read_games(query_obj=query)
