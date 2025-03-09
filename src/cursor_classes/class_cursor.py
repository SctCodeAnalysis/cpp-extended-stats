from typing import List, Union
from clang.cindex import Cursor, CursorKind, AccessSpecifier

from src.cursor_classes.method_cursor import MethodCursor
from src.cursor_classes.attribute_cursor import AttributeCursor


class ClassCursor:
    """The ClassCursor class represents a reference to a class/struct within the AST."""

    # dict with CursorKind as key and class that represents cursor as value
    __cursor_kind_class = {
        CursorKind.FIELD_DECL: AttributeCursor,
        CursorKind.CXX_METHOD: MethodCursor,
    }

    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def get_methods(self) -> List[MethodCursor]:
        """Finds all available methods in the class."""
        return self._get_cursors(CursorKind.CXX_METHOD)

    def get_attributes(self) -> List[AttributeCursor]:
        """Finds all available methods in the class."""
        return self._get_cursors(CursorKind.FIELD_DECL)

    def _get_cursors(self, cursor_kind: Union[CursorKind.FIELD_DECL, CursorKind.CXX_METHOD],
                     visited: tuple[str, str] = None) -> \
            Union[List[AttributeCursor], List[MethodCursor]]:
        """
        Finds all available cursors of specific type in the class.

        :param cursor_kind: Cursor to look for
        :param visited: Set of tuple[filename, class_name] to prevent visiting one class twice
        :return: List[AttributeCursor]
        """
        if visited is None:
            visited = set()
        if (self.cursor.location.file.name, self.cursor.spelling) in visited:
            return []
        visited.add((self.cursor.location.file.name, self.cursor.spelling))

        cursors = []
        for child in self.cursor.get_children():
            # Cursors of given class
            if child.kind == cursor_kind:
                cursors.append(self.__cursor_kind_class[cursor_kind](child))

            # Public and protected cursors of base classes
            if child.kind == CursorKind.CXX_BASE_SPECIFIER:
                base_class = ClassCursor(child.type.get_declaration())
                for cur in base_class._get_cursors(cursor_kind, visited):
                    if cur.access_specifier == AccessSpecifier.PRIVATE:
                        continue

                    if child.access_specifier != AccessSpecifier.PUBLIC:
                        cur.access_specifier = child.access_specifier

                    cur.inherited = True
                    cursors.append(cur)
        return cursors
