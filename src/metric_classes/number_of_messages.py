""" Class that calculates average number of messages. """

from clang.cindex import CursorKind

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor
from src.cursor_classes.method_cursor import MethodCursor


class AverageNumberOfMessages(ClassMetric):
    """ Calculates average number of messages. """

    NAME = "AVERAGE_NUMBER_OF_MESSAGES"

    def __init__(self):
        self._number_of_messages = {}

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        key = (class_cursor.cursor.location.file.name, class_cursor.cursor.spelling)
        self._number_of_messages[key] = 0

        for child in class_cursor.cursor.get_children():
            if child.kind == CursorKind.CXX_METHOD:
                self._number_of_messages[key] += self._consume_method(MethodCursor(child))

    def _consume_method(self, method_cursor: MethodCursor) -> int:
        methods_calls = 0
        for child in method_cursor.cursor.walk_preorder():
            if child.kind == CursorKind.CALL_EXPR and child.referenced:
                print(child.spelling)
                methods_calls += 1
        return methods_calls

    @property
    def result(self) -> float:
        if len(self._number_of_messages) == 0:
            return 0
        return sum(self._number_of_messages.values()) / len(self._number_of_messages)
