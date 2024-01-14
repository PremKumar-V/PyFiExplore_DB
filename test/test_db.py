import os
import pytest
import sqlite3

from app.database.db import Database


@pytest.fixture
def db_instance():
    test_db_name = "test_database.db"
    db = Database(test_db_name)
    yield db
    os.remove(test_db_name)


def test_connect_db(db_instance):
    conn, curr = db_instance.connectDB()
    assert isinstance(conn, sqlite3.Connection)
    assert isinstance(curr, sqlite3.Cursor)
    conn.close()


def test_create_table(db_instance):
    db_instance.createTable()
    conn, curr = db_instance.connectDB()
    curr.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='Database';"
    )
    result = curr.fetchone()
    assert result is not None
    conn.close()
