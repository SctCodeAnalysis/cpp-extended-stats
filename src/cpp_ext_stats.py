""" Class for creating report about quality of C/C++ repository. """

import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from typing import List

from src.metric_classes.number_of_files import NumberOfFiles
from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.class_metric import ClassMetric
from src.metric_classes.attribute_hiding_factor import AttributeHidingFactor
from src.metric_classes.method_hiding_factor import MethodHidingFactor
from src.metric_classes.attribute_inheritance_factor import AttributeInheritanceFactor
from src.metric_classes.method_inheritance_factor import MethodInheritanceFactor
from src.metric_classes.polymorphism_factor import PolymorphismFactor
from src.metric_classes.depth_of_inheritance_tree import AverageDepthOfInheritanceTree


class CppExtStats:
    """Class for calculating metrics of C++ code."""

    def __init__(self, repo_path: str):
        """
        :param repo_path: Path to the repository to analyse
        """
        self._repo_path: str = repo_path
        number_of_files = NumberOfFiles(repo_path)
        self._metrics = {NumberOfFiles.NAME: number_of_files,
                         NumberOfClasses.NAME: NumberOfClasses(number_of_files.get_files()),
                         AttributeHidingFactor.NAME: AttributeHidingFactor(),
                         MethodHidingFactor.NAME: MethodHidingFactor(),
                         AttributeInheritanceFactor.NAME: AttributeInheritanceFactor(),
                         MethodInheritanceFactor.NAME: MethodInheritanceFactor(),
                         PolymorphismFactor.NAME: PolymorphismFactor(),
                         AverageDepthOfInheritanceTree.NAME: AverageDepthOfInheritanceTree()}
        self._calculate()

    def list(self) -> List[str]:
        """
        :return: list of available metrics
        """
        return list(self._metrics.keys())

    def metric(self, metric_name: str) -> float:
        """
        Calculates metric.

        :param metric_name: Name of one of the available metrics
        :return: Calculated value.
        """
        return self._metrics[metric_name].result

    def as_xml(self) -> str:
        """
        Generates an XML report that includes all available metrics.

        :return: XML file as a string
        """
        root = ET.Element("report")
        ET.SubElement(root, "report-time").text = datetime.today().strftime('%d.%m.%Y')
        ET.SubElement(root, "repository-path").text = f"./{self._repo_path}"
        metrics_element = ET.SubElement(root, "metrics")
        for metric in self._metrics.values():
            ET.SubElement(metrics_element, "metric",
                          name=metric.NAME).text = str(round(metric.result, 2))

        return minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")

    def _calculate(self) -> None:
        """Calls callback method of every metric class"""
        for cls in self._metrics[NumberOfClasses.NAME].get_classes():
            for metric in self._metrics.values():
                if isinstance(metric, ClassMetric):
                    metric.consume(cls)
