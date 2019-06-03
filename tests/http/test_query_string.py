from opyapi.http.query_string import parse_qs, QueryString


def test_parse_qs_with_no_value():
    result = parse_qs("")
    assert isinstance(result, dict)
    assert result == {}


def test_parse_qs_with_single_value():
    result = parse_qs("simple_example=test_value")
    assert "simple_example" in result
    assert result["simple_example"] == "test_value"


def test_parse_qs_with_multiple_values():
    result = parse_qs("test_1=1&test_2=2&test_3=3")
    assert result == {
        "test_1": "1",
        "test_2": "2",
        "test_3": "3"
    }


def test_parse_qs_with_array_values():
    result = parse_qs("test_1[]=1&test_1[]=2&test_1[]=3")
    assert result == {
        "test_1": ["1", "2", "3"]
    }


def test_parse_qs_with_dict_values():
    result = parse_qs("test_1[a]=1&test_1[b]=2&test_1[c]=3")
    assert result == {
        "test_1": {
            "a": "1",
            "b": "2",
            "c": "3"
        }
    }


def test_parse_qs_with_nested_arrays():
    result = parse_qs("test_1[][]=1&test_1[][]=2&test_1[][]=3")
    assert result == {
        "test_1": [
            ["1"],
            ["2"],
            ["3"]
        ]
    }


def test_parse_qs_with_indexed_arrays():
    result = parse_qs("test_1[0][]=1&test_1[0][]=2&test_1[0][]=3")
    assert result == {
        "test_1": {
            "0": ["1", "2", "3"],
        }
    }


def test_parse_qs_with_broken_key():
    result = parse_qs("test_1[[a][b]]=1&test_1[b]=2&test_1[c]=3")
    assert result == {
        "test_1[[a][b]]": "1",
        "test_1": {
            "b": "2",
            "c": "3"
        }
    }


def test_query_string_instantiation():
    instance = QueryString("test_1[0][]=1&test_1[0][]=2&test_1[0][]=3")

    assert "test_1" in instance
    assert instance["test_1"] == {
        "0": ["1", "2", "3"]
    }
