from abc import ABC, abstractmethod

from src.cursor_classes.class_cursor import ClassCursor


class ClassMetric(ABC):
    """ Base class for metrics that are connected with Object-Oriented Design """

    NAME = "METRIC_NAME"

    @property
    def result(self) -> float:
        return 0

    @abstractmethod
    def consume(self, class_cursor: ClassCursor) -> None:
        """
        Callback method for processing single reference to a class/struct within the AST.

        :param class_cursor: Reference to a class/struct within the AST
        :return: None
        """
        pass
