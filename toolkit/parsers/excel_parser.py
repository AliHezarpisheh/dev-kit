"""Contains the ExcelParser class for parsing Excel files."""

from typing import Any

import pandas as pd

from .base import Parser


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
        except FileNotFoundError:
            print(f"This path is unreachable: `{self.file_path}`!")
        except pd.errors.ParserError:
            print(f"Error parsing Excel file: `{self.file_path}`!")
