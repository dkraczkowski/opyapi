from opyapi.utils import DocString


def func_with_short_description():
    """
    Short description
    """
    pass


def func_with_long_description():
    """
    Short description

    Long description is here
        with indent support
    """
    pass


def func_with_parameters(a, b, c, d):
    """
    Short description

    Long description is here
        And some addional stuff with indent.
    :param a:
    :param int b:
    :param str c: C description
    :parameter d: D description
    """
    pass


def test_parse_short_description():
    doc = DocString(func_with_short_description)
    assert len(doc.components) == 0
    assert doc.short_description == "Short description"
    assert doc.long_description == ""


def test_parse_long_description():
    doc = DocString(func_with_long_description)
    assert len(doc.components) == 0
    assert doc.short_description == "Short description"
    assert doc.long_description == "Long description is here\n    with indent support"


def test_find_by_type():
    doc = DocString(func_with_parameters)
    params = doc.find_component_by_type("param")
    assert len(params) == 3
    assert params[0].attributes[-1] == "a"
    assert params[1].attributes[-1] == "b"
    assert params[2].attributes[-1] == "c"
    assert params[2].description == "C description"


def test_find_by_multiple_types():
    doc = DocString(func_with_parameters)
    params = doc.find_component_by_type("param", "parameter")
    assert len(params) == 4
    assert params[0].attributes[-1] == "a"
    assert params[1].attributes[-1] == "b"
    assert params[2].attributes[-1] == "c"
    assert params[3].attributes[-1] == "d"
    assert params[2].description == "C description"
    assert params[3].description == "D description"
