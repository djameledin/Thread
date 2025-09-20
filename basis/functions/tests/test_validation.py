import pytest
from ..validation import find_th_files

def test_find_th_files(tmp_path):
    th_file = tmp_path / "test.th"
    th_file.write_text("dummy")

    found_files = find_th_files(tmp_path)

    assert str(th_file) in found_files

def test_find_no_files(tmp_path):
    found_files = find_th_files(tmp_path)
    assert found_files == []
