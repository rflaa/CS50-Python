from plates import is_valid

def test_default():
    assert is_valid("CS50") == True

def test_beggining():
    assert is_valid("1CS50") == False
    assert is_valid("C150") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("CS50111") == False

def test_numbers():
    assert is_valid("CS50A1") == False

def test_zero():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("CS!50") == False
