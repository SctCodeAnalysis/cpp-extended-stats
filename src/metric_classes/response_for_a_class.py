""" Class that calculates average response for a class. """

from clang.cindex import CursorKind

from src.cursor_classes.method_cursor import MethodCursor
from src.metric_classes.method_metric import MethodMetric


class AverageResponseForAClass(MethodMetric):
    """ Calculates average response for a class. """

    NAME = "AVERAGE_RESPONSE_FOR_A_CLASS"

    def __init__(self):
        self._response_for_a_class = {}

    def consume(self, method_cursor: MethodCursor) -> None:
        """
        Callback method for processing single reference to a method within the AST.

        :param method_cursor: Reference to a method within the AST
        :return: None
        """

        if not method_cursor.definition:
            return

        cls = method_cursor.definition.semantic_parent
        key = (cls.location.file.name, cls.spelling)
        if key not in self._response_for_a_class:
            self._response_for_a_class[key] = set()
        self._response_for_a_class[key].add(f"{cls.spelling}::{method_cursor.definition.spelling}")

        for child in method_cursor.definition.walk_preorder():
            if child.kind == CursorKind.CALL_EXPR and child.referenced:
                self._response_for_a_class[key].add(
                    f"{child.referenced.semantic_parent.spelling}::{child.spelling}")

    @property
    def result(self) -> float:
        if len(self._response_for_a_class) == 0:
            return 0
        return sum(map(len, self._response_for_a_class.values())) / len(self._response_for_a_class)
