from flask import Blueprint, send_from_directory, send_file
from config.config import Config
import os

resources_scope = Blueprint('resources_scope', __name__)


@resources_scope.route('/covers/<book_covername>', methods=['GET'])
def send_cover(book_covername):
    directory = os.path.join(Config.STATIC_FOLDER, 'covers')
    return send_from_directory(directory, book_covername)


@resources_scope.route('/download_book/<book_filename>', methods=['GET'])
def dowload_book(book_filename):
    directory = os.path.join(Config.STATIC_FOLDER, 'books', book_filename)
    return send_file(directory)

