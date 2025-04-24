import sqlite3
import os
import db.database as db

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_file: str):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_file)
        return cls._instance

    def _initialize(self, db_file):
        if not os.path.exists(db_file):
            db.create_database(db_file)
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params=None):
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
        DatabaseConnection._instance = None
