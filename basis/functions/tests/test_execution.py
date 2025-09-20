import pytest
from ..execution import execute_commands

def test_upper_command():
    result = execute_commands("hello", ["UPPER"])
    assert result.strip() == "HELLO"

def test_lower_command():
    result = execute_commands("HELLO", ["lower"])
    assert result.strip() == "hello"

def test_reverse_command():
    result = execute_commands("hello", ["esrever"])
    assert result.strip() == "olleh"

def test_remove_vowels():
    result = execute_commands("beautiful", ["nvwls"])
    assert result.strip() == "btfl"
