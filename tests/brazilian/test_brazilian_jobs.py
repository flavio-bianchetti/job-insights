# from src.brazilian_jobs import read_brazilian_file
from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_list = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    jobs_keys = set(key for dict in jobs_list for key in dict.keys())
    expected = ["title", "salary", "type"]
    assert all((key in expected) for key in jobs_keys)
