import pytest

from src.cpp_ext_stats import CppExtStats
from src.metric_classes.number_of_files import NumberOfFiles
from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.method_hiding_factor import MethodHidingFactor
from src.metric_classes.attribute_hiding_factor import AttributeHidingFactor


class TestCppExtStats:
    __repo_paths = ["tests/data/empty",
                    "tests/data/gitignore",
                    "tests/data/inheritance/multiple",
                    "tests/data/inheritance/private",
                    "tests/data/inheritance/protected",
                    "tests/data/inheritance/public",
                    "tests/data/inheritance",
                    "tests/data/several_classes_in_file",
                    "tests/data"]

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 10, 1, 2, 2, 2, 8, 1, 22]))
    )
    def test_number_of_files(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(NumberOfFiles.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 4, 2, 2, 2, 11, 4, 16]))
    )
    def test_number_of_classes(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(NumberOfClasses.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 0, 1, 1, 0.5, 10 / 21, 0, 10 / 22]))
    )
    def test_method_hiding_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(MethodHidingFactor.NAME)

        assert result == expected

    @pytest.mark.parametrize(
        "repo_path, expected",
        list(zip(__repo_paths, [0, 0, 0, 1, 1, 0.5, 10 / 21, 0, 10 / 21]))
    )
    def test_attribute_hiding_factor(self, repo_path, expected):
        stats = CppExtStats(repo_path)
        result = stats.metric(AttributeHidingFactor.NAME)

        assert result == expected
