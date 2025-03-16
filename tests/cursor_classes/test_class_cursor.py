import pytest
from clang.cindex import AccessSpecifier

from src.metric_classes.number_of_classes import NumberOfClasses
from src.metric_classes.number_of_files import NumberOfFiles


class TestClassCursor:
    __access = {AccessSpecifier.PRIVATE: "private",
                AccessSpecifier.PROTECTED: "protected",
                AccessSpecifier.PUBLIC: "public"}

    __args = [("tests/data/inheritance/private", "private_inheritance_fixture"),
              ("tests/data/inheritance/protected", "protected_inheritance_fixture"),
              ("tests/data/inheritance/public", "public_inheritance_fixture"),
              ("tests/data/inheritance/multiple", "multiple_inheritance_fixture"),
              ("tests/data/empty", "empty_fixture")]

    @pytest.mark.parametrize("repo_path, fixture", __args)
    def test_get_methods(self, repo_path, fixture, request):
        number_of_files = NumberOfFiles(repo_path)
        number_of_classes = NumberOfClasses(number_of_files.get_files())

        result = {
            cls.cursor.spelling: {
                f"{atr.cursor.semantic_parent.spelling}::{atr.cursor.spelling}": atr.access_specifier
                for atr in cls.get_methods()
            }
            for cls in number_of_classes.get_classes()
        }

        expected = {
            cls: {
                name + "Method": spec
                for name, spec in d.items()
            }
            for cls, d in request.getfixturevalue(fixture).items()
        }

        assert result == expected

    @pytest.mark.parametrize("repo_path, fixture", __args)
    def test_get_attributes(self, repo_path, fixture, request):
        number_of_files = NumberOfFiles(repo_path)
        number_of_classes = NumberOfClasses(number_of_files.get_files())

        result = {
            cls.cursor.spelling: {
                f"{atr.cursor.semantic_parent.spelling}::{atr.cursor.spelling}": atr.access_specifier
                for atr in cls.get_attributes()
            }
            for cls in number_of_classes.get_classes()
        }

        expected = {
            cls: {
                name + "Attribute": spec
                for name, spec in d.items()
            }
            for cls, d in request.getfixturevalue(fixture).items()
        }

        assert result == expected


@pytest.fixture
def private_inheritance_fixture():
    return {
        "Derived": {
            "Base::protected": AccessSpecifier.PRIVATE,
            "Base::public": AccessSpecifier.PRIVATE},
        "DerivedDerived": {}
    }


@pytest.fixture
def protected_inheritance_fixture():
    return {
        "Derived": {
            "Base::protected": AccessSpecifier.PROTECTED,
            "Base::public": AccessSpecifier.PROTECTED},
        "DerivedDerived": {
            "Base::protected": AccessSpecifier.PROTECTED,
            "Base::public": AccessSpecifier.PROTECTED
        }
    }


@pytest.fixture
def public_inheritance_fixture():
    return {
        "Derived": {
            "Base::protected": AccessSpecifier.PROTECTED,
            "Base::public": AccessSpecifier.PUBLIC},
        "DerivedDerived": {
            "Base::protected": AccessSpecifier.PROTECTED,
            "Base::public": AccessSpecifier.PUBLIC
        }
    }


@pytest.fixture
def multiple_inheritance_fixture():
    return {
        "Base": {"Base::base": AccessSpecifier.PUBLIC},
        "A": {"A::a": AccessSpecifier.PUBLIC, "Base::base": AccessSpecifier.PUBLIC},
        "B": {"B::b": AccessSpecifier.PUBLIC, "Base::base": AccessSpecifier.PUBLIC},
        "Derived": {
            "A::a": AccessSpecifier.PUBLIC,
            "B::b": AccessSpecifier.PUBLIC,
            "Base::base": AccessSpecifier.PUBLIC
        }
    }


@pytest.fixture
def empty_fixture():
    return {}
