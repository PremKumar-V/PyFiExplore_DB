import os
import sqlite3
from datetime import datetime


class Database:
    def __init__(self, dbName: str) -> None:
        self.dbName: str = dbName

    def connectDB(self) -> (sqlite3.Connection, sqlite3.Cursor):
        try:
            conn: sqlite3.Connection = sqlite3.connect(self.dbName)
            curr: sqlite3.Cursor = conn.cursor()

            return (conn, curr)
        except Exception as error:
            print(f"Error: Connecting Phase: {datetime.now()}: {error}")

    def createTable(self) -> None:
        try:
            conn, curr = self.connectDB()

            curr.execute(
                """
                CREATE TABLE Database (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    extension TEXT,
                    is_folder BOOLEAN,
                    path TEXT
                );
                """
            )

            conn.close()
        except Exception as error:
            print(f"Error: Table Creating Phase: {datetime.now()}: {error}")
    
    def insert_folder_file(self, folder_path):
        try:
            conn, curr = self.connectDB()

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    name, extension = os.path.splitext(file)
                    is_folder = False

                    curr.execute("""
                        INSERT INTO Database (name, extension, is_folder, path)
                        VALUES (?, ?, ?, ?)
                    """, (name, extension, is_folder, file_path))

                for directory in dirs:
                    dir_path = os.path.join(root, directory)
                    is_folder = True

                    curr.execute("""
                        INSERT INTO Database (name, extension, is_folder, path)
                        VALUES (?, ?, ?, ?)
                    """, (directory, None, is_folder, dir_path))

            conn.commit()
            conn.close()
        except Exception as error:
            print(f"Error: Insertion Phase: {datetime.now()}: {error}")