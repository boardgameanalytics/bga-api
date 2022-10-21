from datetime import date
from typing import List, Optional, Literal, Union

from pydantic import BaseModel, constr, Extra

GROUP_BY_FIELDS = Literal['artist', 'category', 'designer', 'mechanic', 'publisher']
ORDER_BY_FIELDS = Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating',
                          'total_ratings', 'std_ratings', 'weight', 'popularity']

FILTER_COLS = Literal[
    'release_year', 'avg_rating', 'bayes_rating', 'total_ratings', 'std_ratings', 'min_players', 'max_players',
    'min_playtime', 'max_playtime', 'min_age', 'weight', 'owned_copies', 'wishlist', 'kickstarter', 'popularity',
    'mechanics', 'categories', 'artists', 'publishers', 'designers'
]

GRAPH_COLS = Literal[
    'release_year', 'avg_rating', 'bayes_rating', 'total_ratings', 'std_ratings', 'min_players', 'max_players',
    'min_playtime', 'max_playtime', 'min_age', 'weight', 'owned_copies', 'wishlist', 'popularity'
]


class ExtraForbid(BaseModel):
    class Config:
        extra = Extra.forbid


class Game(ExtraForbid):
    game_id: int
    title: constr(max_length=100)
    release_year: date
    avg_rating: float
    bayes_rating: float
    total_ratings: int
    std_ratings: float
    min_players: int
    max_players: int
    min_playtime: int
    max_playtime: int
    min_age: int
    weight: float
    owned_copies: int
    wishlist: int
    kickstarter: bool
    popularity: float


class FullGame(Game):
    mechanics: List[constr(max_length=100)]
    categories: List[constr(max_length=100)]
    artists: List[constr(max_length=100)]
    publishers: List[constr(max_length=100)]
    designers: List[constr(max_length=100)]
    description: constr(max_length=2000)


class GroupSummary(ExtraForbid):
    name: str
    earliest_release: date
    latest_release: date
    avg_rating: float
    bayes_rating: float
    total_ratings: int
    std_ratings: float
    weight: float
    popularity: float


class Filter(ExtraForbid):
    field: Literal[FILTER_COLS]
    value: Union[str, int, float]  # ToDo: clean str input to prevent SQL Injection attacks
    operator: Literal['=', '<', '>']


class GameQuery(ExtraForbid):
    filter_by: Optional[List[Filter]]
    order_by: Literal['game_id', 'title', 'release_year', 'avg_rating', 'bayes_rating', 'total_ratings', 'std_ratings',
                      'min_players', 'max_players', 'min_playtime', 'max_playtime', 'min_age', 'weight', 'owned_copies',
                      'wishlist', 'popularity']
    ascending: bool
    limit: Optional[int] = 20


class GraphQuery(ExtraForbid):
    x_axis: Literal[GRAPH_COLS]
    y_axis: Optional[Literal[GRAPH_COLS]]
    filter_by: Optional[List[Filter]]
