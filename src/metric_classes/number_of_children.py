""" Class that calculates average number of children metric. """

from clang.cindex import CursorKind

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class AverageNumberOfChildren(ClassMetric):
    """ Calculates average number of children """

    NAME = "AVERAGE_NUMBER_OF_CHILDREN"

    def __init__(self):
        self._number_of_children = {}

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        key = (class_cursor.cursor.location.file.name, class_cursor.cursor.spelling)
        self._number_of_children[key] = self._number_of_children.get(key, 0)

        for child in class_cursor.cursor.get_children():
            if child.kind == CursorKind.CXX_BASE_SPECIFIER:
                base_class = ClassCursor(child.type.get_declaration())

                base_key = (base_class.cursor.location.file.name, base_class.cursor.spelling)
                self._number_of_children[base_key] = self._number_of_children.get(base_key, 0) + 1

    @property
    def result(self) -> float:
        if len(self._number_of_children) == 0:
            return 0
        return sum(self._number_of_children.values()) / len(self._number_of_children)
