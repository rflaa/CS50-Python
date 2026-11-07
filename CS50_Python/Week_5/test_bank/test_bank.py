from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello sir") == 0

def test_h():
    assert value("hi there") == 20
    assert value("h") == 20

def test_greeting():
    assert value("yo") == 100
    assert value("what's up") == 100

def test_numbers():
    assert value("123") == 100

def test_capital():
    assert value("Hello") == 0
    assert value("Hi") == 20
