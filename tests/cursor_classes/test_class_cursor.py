import pytest
from clang.cindex import AccessSpecifier

from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.number_of_files import NumberOfFiles


class TestClassCursor:
    __access = {AccessSpecifier.PRIVATE: "private",
                AccessSpecifier.PROTECTED: "protected",
                AccessSpecifier.PUBLIC: "public"}

    @pytest.mark.parametrize(
        "repo_path, fixture",
        [("tests/data/inheritance/private", "private_inheritance_fixture"),
         ("tests/data/inheritance/protected", "protected_inheritance_fixture"),
         ("tests/data/inheritance/public", "public_inheritance_fixture"),
         ("tests/data/inheritance/multiple", "multiple_inheritance_fixture"),
         ("tests/data/several_classes_in_file", "several_classes_in_file_fixture"),
         ("tests/data/empty", "empty_fixture")]
    )
    def test_get_attributes(self, repo_path, fixture, request):
        number_of_files = NumberOfFiles(repo_path)
        number_of_classes = NumberOfClasses(number_of_files.get_files())

        result = {}
        for cls in number_of_classes.get_classes():
            result[cls.cursor.spelling] = {}
            for atr in cls.get_attributes():
                result[cls.cursor.spelling][atr.cursor.spelling] = self.__access[
                    atr.access_specifier]

        assert result == request.getfixturevalue(fixture)


@pytest.fixture
def private_inheritance_fixture():
    return {
        "Base": {
            "privateBase": "private",
            "protectedBase": "protected",
            "publicBase": "public"},
        "Derived": {
            "protectedBase": "private",
            "publicBase": "private"},
        "DerivedDerived": {}
    }


@pytest.fixture
def protected_inheritance_fixture():
    return {
        "Base": {
            "privateBase": "private",
            "protectedBase": "protected",
            "publicBase": "public"},
        "Derived": {
            "protectedBase": "protected",
            "publicBase": "protected"},
        "DerivedDerived": {
            "protectedBase": "protected",
            "publicBase": "protected"
        }
    }


@pytest.fixture
def public_inheritance_fixture():
    return {
        "Base": {
            "privateBase": "private",
            "protectedBase": "protected",
            "publicBase": "public"},
        "Derived": {
            "protectedBase": "protected",
            "publicBase": "public"},
        "DerivedDerived": {
            "protectedBase": "protected",
            "publicBase": "public"
        }
    }


@pytest.fixture
def multiple_inheritance_fixture():
    return {
        "A": {
            "s_": "private",
            "arr": "public"},
        "B": {"ch": "public"},
        "C": {
            "arr": "public",
            "ch": "public"
        }
    }


@pytest.fixture
def several_classes_in_file_fixture():
    return {
        "A": {
            "privateA": "private",
            "protectedA": "protected",
            "publicA": "public"},
        "B": {"privateB": "private",
              "protectedB": "protected",
              "publicB": "public",
              "publicA": "public",
              "protectedA": "protected"},
        "C": {"privateC": "private",
              "protectedC": "protected",
              "publicC": "public",
              "protectedA": "private",
              "protectedB": "private",
              "publicA": "private",
              "publicB": "private"},
        "D": {
            "privateD": "private",
            "protectedD": "protected",
            "publicD": "public",
            "protectedC": "private",
            "publicC": "private"}
    }


@pytest.fixture
def empty_fixture():
    return {}
