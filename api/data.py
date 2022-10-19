from os import getenv
from typing import List, Dict

from dotenv import load_dotenv
from sqlalchemy import create_engine
from pandas import read_sql_query, DataFrame

from api.schema import Filter, RankQuery


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

    def list_rankings(self, query_obj: RankQuery) -> List[Dict]:
        sql_query = "SELECT * FROM game"

        if query_obj.filter_by:
            sql_query += f" WHERE {' AND '.join([self.parse_filter(item) for item in query_obj.filter_by])}"

        sql_query += f" ORDER BY {query_obj.order_by}"
        if query_obj.ascending:
            sql_query += f" ASC"
        else:
            sql_query += f" DESC"

        sql_query += f" LIMIT {query_obj.limit_results}"

        return self.db.query(query=f"{sql_query};").to_dict(orient='records')
