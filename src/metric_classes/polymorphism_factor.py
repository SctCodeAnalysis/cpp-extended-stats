""" Class that calculates polymorphism factor metric. """

from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class PolymorphismFactor(ClassMetric):
    """ Calculates polymorphism factor """

    NAME = "POLYMORPHISM_FACTOR"

    def __init__(self):
        self._overridden_methods = 0
        self._polymorphic_situations = 0

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.
        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        methods = class_cursor.get_methods()
        inherited_virtual_methods = set((m.cursor.spelling, m.cursor.type.get_canonical().spelling)
                                        for m in methods if m.inherited and m.is_virtual())

        self._polymorphic_situations += len(inherited_virtual_methods)
        for method_cursor in methods:
            if (not method_cursor.inherited and (method_cursor.cursor.spelling,
                                                 method_cursor.cursor.type.get_canonical().spelling)
                    in inherited_virtual_methods):
                self._overridden_methods += 1

    @property
    def result(self):
        if self._polymorphic_situations == 0:
            return 0
        return self._overridden_methods / self._polymorphic_situations
