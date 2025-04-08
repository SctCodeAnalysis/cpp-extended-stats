from typing import List
from clang.cindex import Cursor, CursorKind

from src.cursor_classes.class_cursor import ClassCursor
from src.cursor_classes.method_cursor import MethodCursor


class FileCursor:
    """The FileCursor class represents a reference to a translation unit within the AST."""

    def __init__(self, cursor: Cursor, path: str):
        self.cursor = cursor
        self.path = path

    def get_classes(self) -> List[ClassCursor]:
        """
        Finds class and struct cursors in the file.

        :return: List[ClassCursor]
        """
        return self._get_classes(self.cursor)

    def _get_classes(self, cursor: Cursor) -> List[ClassCursor]:
        if cursor.location.file and cursor.location.file.name != self.path:
            return []
        if cursor.kind in [CursorKind.STRUCT_DECL, CursorKind.CLASS_DECL]:
            return [ClassCursor(cursor)]

        class_cursors = []
        for child in cursor.get_children():
            class_cursors.extend(self._get_classes(child))
        return class_cursors

    def get_methods(self) -> List[MethodCursor]:
        """
        Finds method cursors in the file.

        :return: List[ClassCursor]
        """
        return self._get_methods(self.cursor)

    def _get_methods(self, cursor: Cursor) -> List[MethodCursor]:
        if cursor.location.file and cursor.location.file.name != self.path:
            return []
        if cursor.kind == CursorKind.CXX_METHOD:
            return [MethodCursor(cursor)]

        method_cursors = []
        for child in cursor.get_children():
            method_cursors.extend(self._get_methods(child))
        return method_cursors
