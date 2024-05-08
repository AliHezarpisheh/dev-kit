"""Unit tests for the ExcelParser class."""

from unittest.mock import patch

import pandas as pd
import pytest

from toolkit.parsers import ExcelParser
from toolkit.parsers.helpers.exceptions import ExcelParseError

SAMPLE_EXCEL_CONTENT = pd.DataFrame({"name": ["John"], "age": [30]})

FILE_PATH = "test.xlsx"


@pytest.fixture
def excel_parser() -> ExcelParser:
    """Fixture to instantiate ExcelParser."""
    return ExcelParser(file_path=FILE_PATH)


@pytest.mark.smoke
def test_read(excel_parser: ExcelParser) -> None:
    """Test reading a valid Excel file."""
    with patch("toolkit.parsers.excel_parser.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = SAMPLE_EXCEL_CONTENT
        content = excel_parser.read()

    assert content.shape == SAMPLE_EXCEL_CONTENT.shape
    assert content.columns.tolist() == SAMPLE_EXCEL_CONTENT.columns.tolist()


def test_read_invalid_syntax_excel_file(
    excel_parser: ExcelParser,
) -> None:
    """Test reading an invalid Excel file."""
    with patch("toolkit.parsers.excel_parser.pd.read_excel") as mock_read_excel:
        mock_read_excel.side_effect = pd.errors.ParserError
        with pytest.raises(
            ExcelParseError, match="Error parsing Excel file: `test.xlsx`!"
        ):
            excel_parser.read()
