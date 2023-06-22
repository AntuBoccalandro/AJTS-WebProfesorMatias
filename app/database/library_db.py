from .connection import (
        _fetch_all, 
        _fetch_one, 
        _fetch_none,
)
from ..models.exceptions import BookAlreadyExists, BookNotExists


def insert_book(book_object):
    if book_exists(book_object.book_name):
        raise BookAlreadyExists(f'Book with name={book_object.name} already exists')
    query  = "INSERT INTO library_table (book_name, book_filename, book_covername) VALUES (?, ?, ?)"
    parameters = (book_object.book_name, book_object.book_filename, book_object.book_covername)
    _fetch_none(query, parameters)


def delete_book(book_object):
    if not book_exists(book_object.book_name):
        raise BookNotExists(f'Book with name={book_object.book_name} not exists')
    query  = "DELETE FROM library_table WHERE book_name = ?"
    parameters = (book_object.book_name,)
    _fetch_none(query, parameters)


def list_all():
    query = "SELECT * FROM library_table"
    parameters = None
    record = _fetch_all(query, parameters)
    return record


def list_one(book_object):
    query = "SELECT * FROM library_table WHERE book_name = ?"
    parameters = (book_object.book_name,)
    record = _fetch_one(query, parameters)
    return record

def update_book(book_object):
    query = f"""
    UPDATE library_table 
    SET book_name=?, book_filename=?, book_covername=?
    WHERE book_name=?;
    """
    parameters = (
        book_object.book_name, 
        book_object.book_filename,
        book_object.book_covername,
        book_object.book_name,
        )
    _fetch_none(query, parameters)


def book_exists(book_name):
    query = "SELECT COUNT(*) FROM library_table WHERE book_name = ?"
    count = _fetch_one(query, (book_name,))[0]
    return True if count > 0 else False


def resete_table():
    
    query = f"""CREATE TABLE IF NOT EXISTS library_table (
        book_name TEXT,
        book_filename TEXT,
        book_covername TEXT
    )"""

    _fetch_none(query, parameters=None)



