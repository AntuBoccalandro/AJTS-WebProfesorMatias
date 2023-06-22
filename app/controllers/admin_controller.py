from ..database.library_db import (
    list_all,
    list_one,
    insert_book,
    delete_book,
    update_book
)
from ..models.library import Library
from ..helpers.file_deleter import delete_files
from config.config import Config


def lists():
    return list_all()


def insert(book_name, book_filename, book_covername):
    book_object = Library(book_name, book_filename, book_covername)
    insert_book(book_object)


def delete(book_name, book_filename, book_covername):
    book_object = Library(book_name, book_filename, book_covername)
    filename = list_one(book_object)[1]
    covername = list_one(book_object)[2]
    delete_files(Config.FILES_FOLDER+filename, Config.COVERS_FOLDER+covername)
    delete_book(book_object)
