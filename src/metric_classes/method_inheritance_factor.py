""" Class that calculates method inheritance factor metric. """

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class MethodInheritanceFactor(ClassMetric):
    """ Calculates method inheritance factor """

    NAME = "METHOD_INHERITANCE_FACTOR"

    def __init__(self):
        self._inherited_methods = 0
        self._total_methods = 0

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.
        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        for method_cursor in class_cursor.get_methods():
            self._total_methods += 1
            if method_cursor.is_inherited():
                self._inherited_methods += 1

    @property
    def result(self):
        if self._total_methods == 0:
            return 0
        return self._inherited_methods / self._total_methods
