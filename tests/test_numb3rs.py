from numb3rs import validate

def test_dot():
    assert validate("192.168.1.1") is True
    assert validate("192。168。1。1") is False
    assert validate("192,168,1,1") is False

def test_number():
    assert validate("152.128.10.1") is True
    assert validate("256.1.1.1") is False
    assert validate("198.258.1.1") is False
    assert validate("177.200.289.1") is False
    assert validate("144.221.111.300") is False

def test_length():
    assert validate("1222.120.1.1") is False
    assert validate("122.2324.1.1") is False
    assert validate("123.222.6666.1") is False
    assert validate("211.111.166.4444") is False
