from bank import greeting

def test_hello():
    assert greeting("hello") == "$0"

def test_h():
    assert greeting("h") == "$20"

def test_str():
    assert greeting("What's up?") == "$100"
    assert greeting("abc") == "$100"
    assert greeting("Fuck you. ") == "$100"
