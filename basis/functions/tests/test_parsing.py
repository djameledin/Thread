import pytest
from ..parsing import parse_filename

def test_parse_valid_filename():
    text, commands = parse_filename('return(type["hello"], UPPER.lower)')
    assert text == "hello"
    assert commands == ["UPPER", "lower"]

def test_parse_no_commands():
    text, commands = parse_filename('return(type["hi"])')
    assert text == "hi"
    assert commands == []

def test_parse_invalid_filename():
    with pytest.raises(ValueError):
        parse_filename("wrongformat.th")
