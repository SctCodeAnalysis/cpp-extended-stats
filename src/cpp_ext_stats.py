import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import List

import main
from metric_list import metric_list


class CppExtStats:
    """Class for calculating metrics of C++ code."""

    __metrics: List[str] = metric_list.copy()

    def __init__(self, repo_path: str):
        """
        :param repo_path: Path to the repository to analyse
        """
        self._repo_path = repo_path

    def list(self) -> List[str]:
        """
        :return: list of available metrics
        """
        return CppExtStats.__metrics

    def metric(self, metric_name) -> float:
        """
        Calculates metric.

        :param metric_name: Name of one of the available metrics

        :return: Calculated value.
        """
        pass

    def as_xml(self) -> str:
        """
        Generates an XML report that includes all available metrics.

        :return: XML file as a string
        """
        root = ET.Element("repository", name=self._repo_path)
        number_of_files = ET.SubElement(root, "NUMBER_OF_FILES")
        number_of_files.text = "Number of files"

        return minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")


if __name__ == '__main__':
    main.main()
