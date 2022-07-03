# from src.counter import count_ocurrences
from src.counter import count_ocurrences


def test_counter():
    words = ["python", "javascript"]
    expected = [1639, 122]
    result = []
    for word in words:
        result.append(count_ocurrences("src/jobs.csv", word))
    assert all((value in expected) for value in result)
