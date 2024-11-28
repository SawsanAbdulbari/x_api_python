import os


def is_directory_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)