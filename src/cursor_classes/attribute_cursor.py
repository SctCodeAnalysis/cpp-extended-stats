""" Class represents a reference to an attribute of a class/struct within the AST. """

from clang.cindex import Cursor, AccessSpecifier


class AttributeCursor:
    """
    The AttributeCursor class represents a reference to an
    attribute of a class/struct within the AST.
    """

    def __init__(self, cursor: Cursor):
        self.cursor = cursor
        self.access_specifier = cursor.access_specifier
        self.inherited = False

    def is_hidden(self) -> bool:
        """ Method for checking whether a cursor is hidden. """
        return self.access_specifier in [AccessSpecifier.PRIVATE, AccessSpecifier.PROTECTED]

    def is_inherited(self) -> bool:
        """ Method for checking whether a cursor is inherited. """
        return self.inherited
