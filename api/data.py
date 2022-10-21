from os import getenv
from typing import List, Dict

from dotenv import load_dotenv
from sqlalchemy import create_engine
from pandas import read_sql_query, DataFrame

from api.schema import Filter, GameQuery


class SQL:
    """Wrapper for SQL database interactions"""
    def __init__(self):
        load_dotenv()
        self.engine = create_engine(getenv('DB_URI'))

    def query(self, query: str) -> DataFrame:
        return read_sql_query(query, self.engine)


class BoardgamesDB:
    def __init__(self):
        self.db = SQL()

    @staticmethod
    def parse_filter(f: Filter) -> str:
        return f"{f.field}{f.operator}{f.value}"

    def read_games(self, query_obj: GameQuery) -> List[Dict]:
        sql_query = "SELECT * FROM game"

        if query_obj.filter_by:
            sql_query += f" WHERE {' AND '.join([self.parse_filter(item) for item in query_obj.filter_by])}"

        sql_query += f"""
        ORDER BY {query_obj.order_by} {"ASC" if query_obj.ascending else "DESC"} 
        LIMIT {query_obj.limit}"""

        return self.db.query(query=f"{sql_query};").to_dict(orient='records')

    def group_query(self, group_type: str, order_by: str, ascending: bool, limit: int) -> List[Dict]:
        query = f"""
        SELECT
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
        GROUP BY t.name
        ORDER BY {order_by} {"ASC" if ascending else "DESC"}
        {f"LIMIT {limit}" if limit > 0 else ""};
        """
        return self.db.query(query=query).to_dict(orient='records')
