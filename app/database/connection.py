"""
Connection lo que hace es conectarse a la base de datos y crear funciones que permitan ejecutar las consultas a más bajo nivel, es decir, estás funciones las llamarán desde library_db para poder funcionar como ORM, pero que la capa de base de datos este más protegida.
"""

from contextlib import contextmanager
import sqlite3
from config.config import Config


DATABASE_PATH = Config.DATABASE_PATH

@contextmanager
def __get_cursor():
    connection: sqlite3.Connection = sqlite3.connect(DATABASE_PATH)
    cursor: sqlite3.Cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def _fetch_one(query, parameters):
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchone()


def _fetch_all(query, parameters):
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchall()


def _fetch_none(query, parameters):
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)


def _fetch_lastrow_id(query, parameters):
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.lastrowid

