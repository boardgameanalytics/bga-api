from typing import Literal

from fastapi import APIRouter

from api.data import BoardgamesDB


Router = APIRouter(
    tags=["Group Operations"],
)
Router.db = BoardgamesDB()

GROUP_BY_FIELDS = Literal['artist', 'category', 'designer', 'mechanic', 'publisher']
ORDER_BY_FIELDS = Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
                          'total_ratings', 'std_ratings', 'weight', 'popularity']


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
    @return List[GameGroup]</pre></code>
    """
    return Router.db.group_query(group_type="artist",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)


@Router.get("/read/categories")
async def read_categories(
        order_by: ORDER_BY_FIELDS = 'name',
        ascending: bool = True,
        limit: int = 0
):
    """List game categories and aggregate statistics of matching games
    <pre><code>
    @param order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
    'total_ratings', 'std_ratings', 'weight', 'popularity']
    @param ascending: bool
    @param limit: int
    @return List[GameGroup]</pre></code>
    """
    return Router.db.group_query(group_type="category",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)


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
    @return List[GameGroup]</pre></code>
    """
    return Router.db.group_query(group_type="designer",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)


@Router.get("/read/mechanics")
async def read_mechanics(
        order_by: ORDER_BY_FIELDS = 'name',
        ascending: bool = True,
        limit: int = 0
):
    """List game mechanics and aggregate statistics of matching games
    <pre><code>
    @param order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
    'total_ratings', 'std_ratings', 'weight', 'popularity']
    @param ascending: bool
    @param limit: int
    @return List[GameGroup]</pre></code>
    """
    return Router.db.group_query(group_type="mechanic",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)


@Router.get("/read/publishers")
async def read_publishers(
        order_by: ORDER_BY_FIELDS = 'name',
        ascending: bool = True,
        limit: int = 100
):
    """List game publishers and aggregate statistics of matching games
    <pre><code>
    @param order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
    'total_ratings', 'std_ratings', 'weight', 'popularity']
    @param ascending: bool
    @param limit: int
    @return List[GameGroup]</pre></code>
    """
    return Router.db.group_query(group_type="publisher",
                                 order_by=order_by,
                                 ascending=ascending,
                                 limit=limit)
