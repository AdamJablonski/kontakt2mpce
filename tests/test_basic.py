"""
Basic tests for kontakt2mpce.
"""

import pytest
from pathlib import Path
from kontakt2mpce import __version__
from kontakt2mpce.converter import convert_nki_to_xpm


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_convert_not_implemented():
    """Test that converter raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        convert_nki_to_xpm(Path("test.nki"), Path("output/"))
