from flask import Flask
from config.config import Config
from flask_compress import Compress
from flask_caching import Cache
from .routes.students import students_scope
from .routes.admin import admin_scope
from .routes.resources import resources_scope
from .routes.login import login_scope
from .routes.errors import errors_scope
from .database.library_db import resete_table

app = Flask(
    __name__,
    static_folder=Config.STATIC_FOLDER, 
    template_folder=Config.TEMPLATE_FOLDER,
)
app.config.from_object(Config)

app.register_blueprint(students_scope, url_prefix='/')
app.register_blueprint(admin_scope, url_prefix='/admin')
app.register_blueprint(resources_scope, url_prefix='/resources')
app.register_blueprint(errors_scope, url_prefix='/error')
app.register_blueprint(login_scope, url_prefix='/')

compress = Compress(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

resete_table()
