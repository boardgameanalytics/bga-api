from datetime import date
from typing import Optional, Literal

from pydantic import BaseModel, constr, Extra


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


class GroupSummary(ExtraForbid):
    id: int
    name: str
    earliest_release: date
    latest_release: date
    avg_rating: float
    bayes_rating: float
    total_ratings: int
    std_ratings: float
    weight: float
    popularity: float


class GamesQuery(ExtraForbid):
    order_by: Literal['title', 'release_year', 'avg_rating', 'bayes_rating', 'total_ratings', 'std_ratings',
                      'min_players', 'max_players', 'min_playtime', 'max_playtime', 'min_age', 'weight', 'owned_copies',
                      'wishlist', 'kickstarter', 'popularity'] = 'popularity'
    ascending: bool = False
    limit: int = 20


class SummaryQuery(ExtraForbid):
    order_by: Literal['name', 'earliest_release', 'latest_release', 'avg_rating', 'bayes_rating', 'total_ratings',
                      'std_ratings', 'weight', 'popularity'] = 'name'
    ascending: bool = True
    limit: int = 100


GRAPH_COLS = Literal[
    'release_year', 'avg_rating', 'bayes_rating', 'total_ratings', 'std_ratings', 'min_players', 'max_players',
    'min_playtime', 'max_playtime', 'min_age', 'weight', 'owned_copies', 'wishlist', 'popularity'
]


class GraphQuery(ExtraForbid):
    x_axis: GRAPH_COLS
    y_axis: Optional[GRAPH_COLS]
