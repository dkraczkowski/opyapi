from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

import pytest

from opyapi.schema.types import Integer
from opyapi.schema.types import Array
from opyapi.schema.validators import validate


class CustomType:
    pass


class ExampleEnum(Enum):
    ONE = 1
    TWO = "2"
    THREE = "three"


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [[], list],
        [[1], list],
        [(), tuple],
        [(1,), tuple],
        [{}, dict],
        [{1}, set],
        [{"a"}, set],
        [{"key": 1}, dict],
        [0, int],
        [1, int],
        [1.0, float],
        [1.1, float],
        ["aa", str],
        [True, bool],
        [False, bool],
        [CustomType(), CustomType],
        [1, Any],
        ["1.1", Any],
    ],
)
def test_validate_base_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [[1, ExampleEnum], ["2", ExampleEnum], [ExampleEnum.THREE, ExampleEnum]],
)
def test_validate_enum_definition(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [None, Optional[int]],
        [1, Union[str, int]],
        ["a", Union[str, int]],
        [None, Union[None, int]],
    ],
)
def test_validate_simple_union_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [{}, Dict],
        [{"a": 1}, Dict[str, int]],
        [{"a": 1}, Dict[str, int]],
        [{"a": None}, Dict[str, Optional[int]]],
    ],
)
def test_validate_dict_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [[], List],
        [[1, 2, 3], List[int]],
        [[1, 2, None], List[Optional[int]]],
        [["1", 1], List[Union[str, int]]],
        [["1", "2"], List[str]],
    ],
)
def test_validate_list_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [[], List],
        [[1, 2, 3], List[int]],
        [[1, 2, None], List[Optional[int]]],
        [["1", 1], List[Union[str, int]]],
        [["1", "2"], List[str]],
    ],
)
def test_validate_list_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [
        [[], Sequence],
        [(1,), Sequence],
        [[1], Sequence[int]],
        [("a", "b", None), Sequence[Optional[str]]],
        [[1, 2, 3], Sequence[int]],
    ],
)
def test_validate_sequence_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition",
    [[(1,), Tuple], [("a", "b", None), Tuple[Optional[str]]], [(1, 2, 3), Tuple[int]]],
)
def test_validate_tuple_type_definitions(value, type_definition):
    assert validate(value, type_definition) is None


@pytest.mark.parametrize(
    "value,type_definition", [
        ([1, 2, 3], Array(Integer(minimum=0, maximum=5)))
    ]
)
def test_validate_schema_types(value, type_definition):
    assert validate(value, type_definition) is None
