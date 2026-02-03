import re
import pytest


def format_date(date: str) -> str:
    """Returns input date formated into YYYY-MM-DD"""
    pattern = r"\d{2}/\d{2}/\d{4}"
    if not re.fullmatch(pattern, date):
        raise ValueError("Date must be in format DD/MM/YYYY")
    day, month, year = re.split(r"/", date)
    return f"{year}-{month}-{day}"


def test_format_date_pos():
    assert format_date("05/09/2025") == "2025-09-05"


def test_format_date_exception():
    with pytest.raises(ValueError) as exc_info:
        format_date("05.09.2025")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "Date must be in format DD/MM/YYYY"
