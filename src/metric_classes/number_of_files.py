import os
from typing import List
from clang.cindex import Config, Index

from src.cursor_classes.file_cursor import FileCursor


class NumberOfFiles:
    """
    Collects FileCursors and calculates number of C/C++ files
    """
    __extensions: List[str] = [".cpp", ".h", ".c"]

    def __init__(self, repo_path: str):
        self._name = "NUMBER_OF_FILES"
        self._file_cursors = self._collect_files(repo_path)

    @property
    def name(self) -> str:
        return self._name

    def get_files(self) -> List[FileCursor]:
        return self._file_cursors

    @property
    def result(self) -> int:
        return len(self._file_cursors)

    def _collect_files(self, repo_path: str) -> List[FileCursor]:
        """ Iterates over a folder and collects FileCursors"""

        # Set the path in which to search for libclang
        if not Config.library_file:
            Config.set_library_file("/path/to/libclang.dll")
        index = Index.create()

        file_cursors = []
        for root, _, files in os.walk(repo_path):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext in self.__extensions:
                    cursor = index.parse(os.path.join(root, file), args=['-std=c++17']).cursor
                    file_cursors.append(FileCursor(cursor, os.path.join(root, file)))
        return file_cursors
