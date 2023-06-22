# Developer Config
class Config:
    # SERVER_NAME = "localhost:5000"
    # DEBUG = True

    DATABASE_PATH = "app/database/library_db.db"

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

    FILES_FOLDER = "app/" + STATIC_FOLDER + "books/"
    COVERS_FOLDER = "app/" + STATIC_FOLDER + "covers/"
    
    SECRET_KEY = 'juanantutoto'
