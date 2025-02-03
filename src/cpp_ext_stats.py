import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from typing import List

from src.metric_classes.number_of_files import NumberOfFiles
from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.class_metric import ClassMetric
from src.metric_classes.attribute_hiding_factor import AttributeHidingFactor


class CppExtStats:
    """Class for calculating metrics of C++ code."""

    def __init__(self, repo_path: str):
        """
        :param repo_path: Path to the repository to analyse
        """
        self._repo_path: str = repo_path
        number_of_files = NumberOfFiles(repo_path)
        number_of_classes = NumberOfClasses(number_of_files.get_files())
        self._metrics = {"NUMBER_OF_FILES": number_of_files,
                         "NUMBER_OF_CLASSES": number_of_classes,
                         "ATTRIBUTE_HIDING_FACTOR": AttributeHidingFactor()}
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
            ET.SubElement(metrics_element, metric.name).text = str(round(metric.result, 2))

        return minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")

    def _calculate(self):
        for cls in self._metrics["NUMBER_OF_CLASSES"].get_classes():
            for metric in self._metrics.values():
                if isinstance(metric, ClassMetric):
                    metric.consume(cls)
