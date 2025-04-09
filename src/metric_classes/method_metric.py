""" Base class for metrics. """

from abc import ABC, abstractmethod

from src.cursor_classes.method_cursor import MethodCursor


class MethodMetric(ABC):
    """ Base class for metrics that are connected with Object-Oriented Design """

    NAME = "METRIC_NAME"

    @property
    def result(self) -> float:
        """ Property that returns value of calculated metric. """
        return 0

    @abstractmethod
    def consume(self, method_cursor: MethodCursor) -> None:
        """
        Callback method for processing single reference to a method within the AST.

        :param method_cursor: Reference to a method within the AST
        :return: None
        """
