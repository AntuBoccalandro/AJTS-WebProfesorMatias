import os


def delete_files(*paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)

