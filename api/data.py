from os import getenv
from typing import List, Dict

from dotenv import load_dotenv
from sqlalchemy import create_engine


class SQL:
    """Wrapper for SQL database interactions"""
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(getenv('DB_URI'))

    def query(self, query: str) -> List[Dict]:
        with self.engine.connect() as conn:
            return conn.execute(query).mappings().all()


class BoardgamesDB:
    def __init__(self):
        self.db = SQL()

    def read_games(self, order_by: str, ascending: bool, limit: int) -> List[Dict]:
        sql_query = f"""
        SELECT 
            *
        FROM game
        ORDER BY {order_by} {"ASC" if ascending else "DESC"} 
        LIMIT {limit};
        """

        return self.db.query(query=sql_query)

    def group_summary(self, group_type: str, order_by: str, ascending: bool, limit: int) -> List[Dict]:
        query = f"""
        SELECT
            t.id AS "id",
            t.name AS "name",
            min(g.release_year) AS "earliest_release",
            max(g.release_year) AS "latest_release",
            avg(g.avg_rating) AS "avg_rating",
            avg(g.bayes_rating) AS "bayes_rating",
            avg(g.total_ratings) AS "total_ratings",
            avg(g.std_ratings) AS "std_ratings",
            avg(g.weight) AS "weight",
            avg(g.popularity) AS "popularity"
        FROM game g
        JOIN game_{group_type} rt on g.id = rt.game_id
        JOIN {group_type} t on rt.{group_type}_id = t.id
        GROUP BY t.id, t.name
        ORDER BY {order_by} {"ASC" if ascending else "DESC"}
        {f"LIMIT {limit}" if limit > 0 else ""};
        """
        return self.db.query(query=query)

    def group_games(self,
                    item_type: str,
                    item_id: int,
                    order_by: str,
                    ascending: bool = False,
                    limit: int = 100) -> List[Dict]:
        sql_query = f"""
        SELECT
            g.id,
            g.title,
            g.release_year,
            g.avg_rating,
            g.bayes_rating,
            g.total_ratings,
            g.std_ratings,
            g.min_players,
            g.max_players,
            g.min_playtime,
            g.max_playtime,
            g.min_age,
            g.weight,
            g.owned_copies,
            g.wishlist,
            g.kickstarter,
            g.popularity
        FROM game g 
        JOIN game_{item_type} gt on g.id = gt.game_id
        JOIN {item_type} t on gt.{item_type}_id = t.id
        WHERE t.id = '{item_id}'
        ORDER BY {order_by} {"ASC" if ascending else "DESC"} LIMIT {limit};
        """
        return self.db.query(query=sql_query)
