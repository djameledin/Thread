import pytest
from conflicts import check_command_conflicts

def test_conflict_upper_lower():
    with pytest.raises(ValueError):
        check_command_conflicts(["UPPER", "lower"])

def test_conflict_random_upper():
    with pytest.raises(ValueError):
        check_command_conflicts(["rAndOm", "UPPER"])

def test_no_conflict():
    check_command_conflicts(["UPPER", "esrever"])
