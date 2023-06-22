import os
from config.config import Config


def save_files(*paths):
    for path in paths:

        if not os.path.exists(path[1]):
            path[0].save(path[1])

