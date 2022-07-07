# from src.sorting import sort_by
from src.sorting import sort_by


jobs_list_mock = [
        {"max_salary": 25000, "min_salary": 2500, "date_posted": "2022-06-29"},
        {"max_salary": -1000, "min_salary": 1000, "date_posted": "2022-06-27"},
        {"max_salary": 30000, "min_salary": 2000, "date_posted": "2022-06-28"},
        {"max_salary": 10, "min_salary": 0, "date_posted": "2022-06-26"},
        {"max_salary": 20000, "min_salary": 1100, "date_posted": "2022-06-30"},
        {"max_salary": 10000, "min_salary": 1000, "date_posted": "2022-07-01"},
    ]


criteria_keys = ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria():
    for criteria in criteria_keys:
        sort_by(jobs_list_mock, criteria)
        if criteria == "min_salary":
            assert(jobs_list_mock[0][criteria] <= jobs_list_mock[1][criteria])
        else:
            assert(jobs_list_mock[0][criteria] >= jobs_list_mock[1][criteria])
