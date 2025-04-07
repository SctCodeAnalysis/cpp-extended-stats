import pytest

from src.cpp_ext_stats import CppExtStats
from src.metric_classes.number_of_files import NumberOfFiles
from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.method_hiding_factor import MethodHidingFactor
from src.metric_classes.attribute_hiding_factor import AttributeHidingFactor
from src.metric_classes.method_inheritance_factor import MethodInheritanceFactor
from src.metric_classes.attribute_inheritance_factor import AttributeInheritanceFactor
from src.metric_classes.polymorphism_factor import PolymorphismFactor
from src.metric_classes.depth_of_inheritance_tree import AverageDepthOfInheritanceTree
from src.metric_classes.number_of_children import AverageNumberOfChildren
from src.metric_classes.response_for_a_class import AverageResponseForAClass


class TestCppExtStats:
    __repo_paths = ["tests/data/empty",
                    "tests/data/gitignore",
                    "tests/data/inheritance/multiple",
                    "tests/data/inheritance/private",
                    "tests/data/inheritance/protected",
                    "tests/data/inheritance/public",
                    "tests/data/inheritance",
                    "tests/data/several_classes_in_file"]

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 10, 1, 2, 2, 2, 8, 1]))
    )
    def test_number_of_files(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(NumberOfFiles.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 4, 2, 2, 2, 11, 4]))
    )
    def test_number_of_classes(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(NumberOfClasses.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 0, 1, 1, 0.5, 10 / 21, 0]))
    )
    def test_method_hiding_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(MethodHidingFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 0, 1, 1, 0.5, 10 / 21, 0]))
    )
    def test_attribute_hiding_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AttributeHidingFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 5 / 8, 1, 1, 1, 15 / 21, 0]))
    )
    def test_method_inheritance_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(MethodInheritanceFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 5 / 8, 1, 1, 1, 15 / 21, 0]))
    )
    def test_attribute_inheritance_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AttributeInheritanceFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        [("tests/data/gitignore", 0),
         ("tests/data/polymorphism/standard", 3 / 4),
         ("tests/data/polymorphism/signatures_difference", 1 / 3),
         ("tests/data/polymorphism/multiple_inheritance", 2 / 3),
         ("tests/data/polymorphism/complicated", 6 / 10)]
    )
    def test_polymorphism_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(PolymorphismFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        [("tests/data/empty", 0),
         ("tests/data/hierarchy/mixed", 26 / 12),
         ("tests/data/hierarchy/diamond", 25 / 12),
         ("tests/data/hierarchy", 51 / 24)]
    )
    def test_average_depth_of_inheritance_tree(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AverageDepthOfInheritanceTree.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        [("tests/data/empty", 0),
         ("tests/data/hierarchy/mixed", 14 / 12),
         ("tests/data/hierarchy/diamond", 13 / 12),
         ("tests/data/hierarchy", 27 / 24)]
    )
    def test_average_number_of_children(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AverageNumberOfChildren.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        [("tests/data/empty", 0),
         ("tests/data/method_calls/standard", 5 / 2),
         ("tests/data/method_calls/complicated", 11 / 3),
         ("tests/data/method_calls/several_files", 10 / 3),
         ("tests/data/method_calls", 26 / 8)]
    )
    def test_average_response_for_a_class(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AverageResponseForAClass.NAME)

        assert result == expected
