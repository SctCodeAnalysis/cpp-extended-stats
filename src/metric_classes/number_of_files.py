import os
from collections.abc import Callable
from typing import List

from clang.cindex import Config, Index
from gitignore_parser import parse_gitignore

from src.cursor_classes.file_cursor import FileCursor


class NumberOfFiles:
    """
    Collects FileCursors and calculates number of C/C++ files
    """

    NAME = "NUMBER_OF_FILES"

    __extensions: List[str] = [".h", ".hpp", ".c", ".C", ".cc", ".cpp",
                               ".CPP", ".c++", ".cp", ".cxx"]

    def __init__(self, repo_path: str):
        self._file_cursors = self._collect_files(os.path.normpath(repo_path))

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

        matches_gitignore: Callable[[str], bool] = self._get_matches_gitignore(repo_path)

        file_cursors = []
        for root, _, files in os.walk(repo_path):
            if matches_gitignore(root):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)
                if ext in self.__extensions and not matches_gitignore(file_path):
                    cursor = index.parse(file_path).cursor
                    file_cursors.append(FileCursor(cursor, file_path))
        return file_cursors

    def _get_matches_gitignore(self, repo_path) -> Callable[[str], bool]:
        """ Gets a function for checking whether a file or a dir is in .gitignore """
        gitignore_path = os.path.join(repo_path, ".gitignore")
        if os.path.exists(gitignore_path):
            return parse_gitignore(gitignore_path)
        return lambda x: False
