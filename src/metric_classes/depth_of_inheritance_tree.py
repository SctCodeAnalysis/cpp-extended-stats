""" Class that calculates average depth of inheritance tree metric. """

from clang.cindex import CursorKind

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class AverageDepthOfInheritanceTree(ClassMetric):
    """ Calculates average depth of inheritance tree """

    NAME = "AVERAGE_DEPTH_OF_INHERITANCE_TREE"

    def __init__(self):
        self._depth_of_inheritance = {}

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        key = (class_cursor.cursor.location.file.name, class_cursor.cursor.spelling)
        if key in self._depth_of_inheritance:
            return

        self._depth_of_inheritance[key] = 0
        for child in class_cursor.cursor.get_children():
            if child.kind == CursorKind.CXX_BASE_SPECIFIER:
                base_class = ClassCursor(child.type.get_declaration())
                self.consume(base_class)

                base_key = (base_class.cursor.location.file.name, base_class.cursor.spelling)
                self._depth_of_inheritance[key] = max(self._depth_of_inheritance[key],
                                                      self._depth_of_inheritance[base_key] + 1)

    @property
    def result(self) -> float:
        if len(self._depth_of_inheritance) == 0:
            return 0
        return sum(self._depth_of_inheritance.values()) / len(self._depth_of_inheritance)
