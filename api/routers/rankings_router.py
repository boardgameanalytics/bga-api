from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import RankQuery


Router = APIRouter(
    tags=["Ranking Operations"],
)
Router.db = BoardgamesDB()


@Router.post("/rankings")
async def rank_games(query: RankQuery):
    """Rank games ranked by given metric
    <pre><code>
    @param query: JSON[RankQuery]
    @return List[Game]</pre></code>"""
    return Router.db.list_rankings(query_obj=query)
