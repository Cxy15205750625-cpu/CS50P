from working import convert
import pytest

def test_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_twelve():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"


def test_hour():
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")


def test_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5:60 PM")

    with pytest.raises(ValueError):
        convert("9:5 AM to 5 PM")


def test_separator():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5 PM extra")



