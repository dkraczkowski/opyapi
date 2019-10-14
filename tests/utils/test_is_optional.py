from typing import List
from typing import Optional

import pytest

from opyapi.utils import is_optional
from opyapi.schema.types import String


@pytest.mark.parametrize("type_definition", [
    Optional[List],
    Optional[int],
    Optional[str],
    String(nullable=True),
])
def test_valid_optional_types(type_definition):
    assert is_optional(type_definition)


@pytest.mark.parametrize("type_definition", [
    List[str],
    int,
    str,
    String(),
])
def test_non_optional_types(type_definition):
    assert is_optional(type_definition) is False
