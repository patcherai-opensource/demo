def get_working_directory():
    import pathlib
    return pathlib.Path.cwd()


def get_timestamp():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc)
