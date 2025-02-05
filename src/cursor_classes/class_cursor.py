from typing import List
from clang.cindex import Cursor, CursorKind, AccessSpecifier

from src.cursor_classes.method_cursor import MethodCursor
from src.cursor_classes.attribute_cursor import AttributeCursor


class ClassCursor:
    """The ClassCursor class represents a reference to a class/struct within the AST."""

    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def get_methods(self) -> List[MethodCursor]:
        """Finds all available methods in the class."""
        pass

    def get_attributes(self, visited: tuple[str, str] = None) -> List[AttributeCursor]:
        """
        Finds all available attributes in the class.

        :param visited: Set of tuple[filename, class_name] to prevent visiting one class twice
        :return: List[AttributeCursor]
        """
        if visited is None:
            visited = set()
        if (self.cursor.location.file.name, self.cursor.spelling) in visited:
            return []
        visited.add((self.cursor.location.file.name, self.cursor.spelling))

        attribute_cursors = []
        for child in self.cursor.get_children():
            # Attributes of given class
            if child.kind == CursorKind.FIELD_DECL:
                attribute_cursors.append(AttributeCursor(child))

            # Public and protected attributes of base classes
            if child.kind == CursorKind.CXX_BASE_SPECIFIER:
                for atr in ClassCursor(child.type.get_declaration()).get_attributes(visited):
                    if atr.access_specifier == AccessSpecifier.PRIVATE:
                        continue

                    if child.access_specifier != AccessSpecifier.PUBLIC:
                        atr.access_specifier = child.access_specifier

                    attribute_cursors.append(atr)
        return attribute_cursors
