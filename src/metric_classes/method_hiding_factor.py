from src.metric_classes.class_metric import ClassMetric
from src.cursor_classes.class_cursor import ClassCursor


class MethodHidingFactor(ClassMetric):
    """ Calculates method hiding factor """

    def __init__(self):
        self._name = "METHOD_HIDING_FACTOR"
        self._hidden_methods = 0
        self._total_methods = 0

    @property
    def name(self) -> str:
        return self._name

    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        for method_cursor in class_cursor.get_methods():
            self._total_methods += 1
            if method_cursor.is_hidden():
                self._hidden_methods += 1

    @property
    def result(self):
        if self._total_methods == 0:
            return 0
        return self._hidden_methods / self._total_methods
