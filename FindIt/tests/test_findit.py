import os
from io import StringIO
from unittest.mock import patch
import pytest
from ..scripts.findit import main


def test_main_with_valid_arguments(tmp_path):
    # Create test files
    file1 = tmp_path / "test_file1.pro"
    file2 = tmp_path / "test_file2.rux"
    with open(file1, "w") as f:
        f.write("Hello, find me!")
    with open(file2, "w") as f:
        f.write("This is a test.")

    args = {
        "<string>": "find me",
        "<datadir>": str(tmp_path),
        "<outputfile>": str(tmp_path / "output.txt"),
    }

    main(**args)

    with open(args["<outputfile>"], "r") as f:
        output = f.read()
        assert file1.name in output
        assert file2.name not in output


def test_main_with_invalid_datadir(capsys):
    args = {
        "<string>": "find me",
        "<datadir>": "invalid_path",
        "<outputfile>": "output.txt",
    }

    main(**args)

    captured = capsys.readouterr()
    assert "invalid_path does not exist" in captured.out


def test_main_with_no_matching_files(tmp_path, capsys):
    args = {
        "<string>": "find me",
        "<datadir>": str(tmp_path),
        "<outputfile>": "output.txt",
    }

    main(**args)

    captured = capsys.readouterr()
    assert "Finished in" in captured.out


def test_main_with_version_flag(capsys):
    with pytest.raises(SystemExit):
        with patch("sys.argv", ["findit", "--version"]):
            main()

    captured = capsys.readouterr()
    assert "FindIt, Version:" in captured.out


if __name__ == "__main__":
    pytest.main()
