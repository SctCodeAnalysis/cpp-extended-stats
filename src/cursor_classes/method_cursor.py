""" Class represents a reference to a method of a class/struct within the AST. """

from clang.cindex import Cursor, AccessSpecifier


class MethodCursor:
    """
    The MethodCursor class represents a reference to a
    method of a class/struct within the AST.
    """

    def __init__(self, cursor: Cursor):
        self.cursor = cursor
        self.definition = cursor.get_definition()
        self.access_specifier = cursor.access_specifier
        self.inherited = False

    def is_hidden(self) -> bool:
        """ Method for checking whether a cursor method is hidden. """
        return self.access_specifier in [AccessSpecifier.PRIVATE, AccessSpecifier.PROTECTED]

    def is_inherited(self) -> bool:
        """ Method for checking whether a cursor method is inherited. """
        return self.inherited

    def is_virtual(self) -> bool:
        """ Method for checking whether a cursor method is virtual. """
        return self.cursor.is_virtual_method()
