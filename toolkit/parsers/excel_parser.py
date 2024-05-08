"""Contains the ExcelParser class for parsing Excel files."""

import logging
from typing import Any

import pandas as pd

from .base import Parser
from .helpers.exceptions import ExcelParseError

logger = logging.getLogger(__name__)


class ExcelParser(Parser):
    """Parses Excel files and loads their content."""

    def read(self) -> Any:
        """
        Read a Excel file and return its content as a dictionary.

        Returns
        -------
        Any
            The parsed content of the Excel file.
        """
        try:
            content = pd.read_excel(self.file_path, sheet_name=None)
            return content
        except pd.errors.ParserError:
            msg = f"Error parsing Excel file: `{self.file_path}`!"
            logger.error(msg, exc_info=True)
            raise ExcelParseError(msg)
