from clang.cindex import Cursor, AccessSpecifier


class MethodCursor:
    """
    The MethodCursor class represents a reference to a
    method of a class/struct within the AST.
    """

    def __init__(self, cursor: Cursor):
        self.cursor = cursor
        self.access_specifier = cursor.access_specifier
        self.inherited = False

    def is_hidden(self) -> bool:
        return self.access_specifier in [AccessSpecifier.PRIVATE, AccessSpecifier.PROTECTED]

    def is_inherited(self) -> bool:
        return self.inherited
