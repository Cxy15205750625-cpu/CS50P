from plates import is_valid

def test_length():
    assert not is_valid("a")
    assert not is_valid("ab34567")
    assert is_valid("ac3456")

def test_type():
    assert not is_valid("123456")
    assert not is_valid("a12345")
    assert not is_valid("1a2345")

def test_alnum():
    assert not is_valid("ab 345")
    assert not is_valid("ab!345")
    assert not is_valid("ab:345")

def test_zero():
    assert not is_valid("AB0345")

def test_nmbr_alnum():
    assert not is_valid("ab12cd")

