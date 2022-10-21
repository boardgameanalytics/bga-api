from fastapi import APIRouter

from api.data import BoardgamesDB
from api.schema import GROUP_BY_FIELDS, ORDER_BY_FIELDS


Router = APIRouter(
    tags=["Designers Operations"],
)
Router.db = BoardgamesDB()


@Router.get("/read/designers")
async def read_designers(
        order_by: ORDER_BY_FIELDS = 'name',
        ascending: bool = True,
        limit: int = 100
):
    """List game designers and aggregate statistics of matching games
    <pre><code>
    @param order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
    'total_ratings', 'std_ratings', 'weight', 'popularity']
    @param ascending: bool
    @param limit: int
    @return List[GroupSummary]</pre></code>
    """
    return Router.db.group_query(group_type="designer",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)
