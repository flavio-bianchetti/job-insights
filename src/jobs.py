from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    try:
        with open(path, encoding='utf-8') as file:
            # https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries
            result = [
                {key: value for key, value in row.items()}
                for row in csv.DictReader(file, skipinitialspace=True)
            ]
            return result
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
