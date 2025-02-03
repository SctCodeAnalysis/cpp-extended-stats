from clang.cindex import Cursor


class MethodCursor:
    """
    The MethodCursor class represents a reference to a
    method of a class/struct within the AST.
    """
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def is_inherited(self) -> bool:
        pass
