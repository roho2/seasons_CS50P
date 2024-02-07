import seasons
from datetime import date


def test_create_date_object():
    assert seasons.create_date_object("1999-06-06") == date.fromisoformat("1999-06-06")


def test_display_minutes():
    ...


def test_calculate_minutes():
    ...
