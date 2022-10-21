from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import ORDER_BY_FIELDS


Router = APIRouter(
    tags=["Artists Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/read/artists")
async def read_artists(
        order_by: ORDER_BY_FIELDS = 'name',
        ascending: bool = True,
        limit: int = 100
):
    """List game artists and aggregate statistics of matching games
    <pre><code>
    @param order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
    'total_ratings', 'std_ratings', 'weight', 'popularity']
    @param ascending: bool
    @param limit: int
    @return List[GroupSummary]</pre></code>
    """
    return Router.db.group_query(group_type="artist",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)
