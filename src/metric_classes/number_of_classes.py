""" Class that calculates number of classes metric. """

from typing import List

from src.cursor_classes.class_cursor import ClassCursor
from src.cursor_classes.file_cursor import FileCursor


class NumberOfClasses:
    """
    Collects ClassCursors and calculates number of C/C++ classes
    """

    NAME = "NUMBER_OF_CLASSES"

    def __init__(self, file_cursors: List[FileCursor]):
        """
        :param file_cursors: List of FileCursors, collected in NumberOfFiles class
        """
        self._class_cursors = self._collect_classes(file_cursors)

    @property
    def result(self):
        """ Property that returns number of classes. """
        return len(self._class_cursors)

    def get_classes(self) -> List[ClassCursor]:
        """ Gets list of class cursors. """
        return self._class_cursors

    def _collect_classes(self, file_cursors: List[FileCursor]) -> List[ClassCursor]:
        class_cursors = []
        for file in file_cursors:
            class_cursors.extend(file.get_classes())
        return class_cursors
