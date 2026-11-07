from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_capitals():
    assert shorten("fEaRsOmE") == "fRsm"

def test_blank():
    assert shorten("") == ""

def test_consonants():
    assert shorten("fngv") == "fngv"

def test_vowels():
    assert shorten("aaa") == ""
    assert shorten("eee") == ""
    assert shorten("iii") == ""
    assert shorten("ooo") == ""
    assert shorten("uuu") == ""

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("nickname456") == "ncknm456"

def test_punctuation():
    assert shorten("!!!") == "!!!"
    assert shorten("hello!") == "hll!"
