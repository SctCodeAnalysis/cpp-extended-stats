""" Class that calculates average number of messages. """

from clang.cindex import CursorKind

from src.cursor_classes.method_cursor import MethodCursor
from src.metric_classes.method_metric import MethodMetric


class AverageNumberOfMessages(MethodMetric):
    """ Calculates average number of messages. """

    NAME = "AVERAGE_NUMBER_OF_MESSAGES"

    def __init__(self):
        self._number_of_messages = {}

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
        if key not in self._number_of_messages:
            self._number_of_messages[key] = 0

        for child in method_cursor.definition.walk_preorder():
            if child.kind == CursorKind.CALL_EXPR and child.referenced:
                self._number_of_messages[key] += 1

    @property
    def result(self) -> float:
        if len(self._number_of_messages) == 0:
            return 0
        return sum(self._number_of_messages.values()) / len(self._number_of_messages)
