from pathlib import Path

import pytest

from black_cgx import main


DATA_PATH = Path(__file__).parent / "data"


def test_check(caplog):
    simple_cgx = DATA_PATH / "simple.cgx"

    with pytest.raises(SystemExit) as e:
        main(["--check", str(simple_cgx)])

    assert e.value.code == 1
    assert "Would change" in caplog.text
    assert "simple.cgx" in caplog.text


def test_check_already_formatted(caplog):
    simple_cgx = DATA_PATH / "simple_formatted.cgx"

    main(["--check", str(simple_cgx)])

    assert "Would change" not in caplog.text
    assert "simple.cgx" not in caplog.text
    assert caplog.text == ""
