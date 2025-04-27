import os
import sqlite3
import db.database as db


class DatabaseConnection:
    """
    Singleton class to manage SQLite database connection.
    Ensures only one connection instance exists.
    """

    _instance = None

    def __new__(cls, db_file: str):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize(db_file)
        return cls._instance

    def _initialize(self, db_file: str):
        if not os.path.exists(db_file):
            db.create_database(db_file)
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def execute_query(self, query: str, params=None):
        """
        Executes a query with optional parameters and returns fetched results.
        """
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def commit(self):
        """
        Commits the current transaction.
        """
        self.connection.commit()

    def close(self):
        """
        Closes the database connection and resets the singleton instance.
        """
        self.connection.close()
        DatabaseConnection._instance = None

    def push(self):
        """
        Commits changes and closes the connection.
        """
        self.commit()
        self.close()
