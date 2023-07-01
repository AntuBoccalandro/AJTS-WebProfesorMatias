from datetime import timedelta

# Devlopment Config
class Config:
    # SERVER_NAME = "localhost:5000"
    # DEBUG = True

    DATABASE_PATH = "app/database/library_db.db"

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

    FILES_FOLDER = "app/" + STATIC_FOLDER + "books/"
    COVERS_FOLDER = "app/" + STATIC_FOLDER + "covers/"
    
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=365)
    SECRET_KEY = 'juanantutoto'

    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
