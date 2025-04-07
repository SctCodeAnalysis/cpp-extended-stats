""" Class that calculates average response for a class. """

from clang.cindex import CursorKind

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor
from src.cursor_classes.method_cursor import MethodCursor


class AverageResponseForAClass(ClassMetric):
    """ Calculates average response for a class. """

    NAME = "AVERAGE_RESPONSE_FOR_A_CLASS"

    def __init__(self):
        self._response_for_a_class = {}

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        methods = set()
        for child in class_cursor.cursor.get_children():
            if child.kind == CursorKind.CXX_METHOD:
                methods.add(f"{class_cursor.cursor.spelling}::{child.spelling}")
                self._consume_method(MethodCursor(child), methods)

        key = (class_cursor.cursor.location.file.name, class_cursor.cursor.spelling)
        self._response_for_a_class[key] = len(methods)

    def _consume_method(self, method_cursor: MethodCursor, methods: set):
        for child in method_cursor.cursor.walk_preorder():
            if child.kind == CursorKind.CALL_EXPR and child.referenced:
                methods.add(f"{child.referenced.semantic_parent.spelling}::{child.spelling}")

    @property
    def result(self) -> float:
        if len(self._response_for_a_class) == 0:
            return 0
        return sum(self._response_for_a_class.values()) / len(self._response_for_a_class)
