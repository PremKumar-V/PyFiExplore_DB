import os
from dotenv import load_dotenv
from database.db import Database

load_dotenv()

SEARCH_PATH = os.getenv("SEARCH_PATH")
DB_NAME = os.getenv("DB_PATH")

DB = Database(DB_NAME)

class Optimization:
    def __init__(self) -> None:
        self.conn, self.curr = DB.connectDB()
    

    
