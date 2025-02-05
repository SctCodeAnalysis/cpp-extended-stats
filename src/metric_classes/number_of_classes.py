from typing import List

from src.cursor_classes.class_cursor import ClassCursor
from src.cursor_classes.file_cursor import FileCursor


class NumberOfClasses:
    """
    Collects ClassCursors and calculates number of C/C++ classes
    """

    def __init__(self, file_cursors: List[FileCursor]):
        """
        :param file_cursors: List of FileCursors, collected in NumberOfFiles class
        """
        self._name = "NUMBER_OF_CLASSES"
        self._class_cursors = self._collect_classes(file_cursors)

    @property
    def name(self) -> str:
        return self._name

    @property
    def result(self):
        return len(self._class_cursors)

    def get_classes(self):
        return self._class_cursors

    def _collect_classes(self, file_cursors: List[FileCursor]) -> List[ClassCursor]:
        class_cursors = []
        for file in file_cursors:
            class_cursors.extend(file.get_classes())
        return class_cursors
