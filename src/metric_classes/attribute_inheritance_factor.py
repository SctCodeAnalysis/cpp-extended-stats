from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class AttributeInheritanceFactor(ClassMetric):
    """ Calculates attribute inheritance factor """

    NAME = "ATTRIBUTE_INHERITANCE_FACTOR"

    def __init__(self):
        self._inherited_attributes = 0
        self._total_attributes = 0

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        for attribute_cursor in class_cursor.get_attributes():
            self._total_attributes += 1
            if attribute_cursor.is_inherited():
                self._inherited_attributes += 1

    @property
    def result(self):
        if self._total_attributes == 0:
            return 0
        return self._inherited_attributes / self._total_attributes
