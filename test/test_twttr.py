from twttr import short

def test_upper():
    assert short("TWITTER") == "TWTTR"

def test_lower():
    assert short("twitter") == "twttr"

def test_numbers():
    assert short("CS50P") == "CS50P"


