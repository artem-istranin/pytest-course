import pytest

from uc.converter import ConversionGraph, Quantity


@pytest.fixture(
    scope="class",
    params=["bfs", "dfs"]
)
def unit_registry(request) -> ConversionGraph:
    g = ConversionGraph(search_algo=request.param)

    g.add_unit("m", "length")
    g.add_unit("cm", "length")
    g.add_unit("mm", "length")
    g.add_unit("mi", "length")
    g.add_unit("km", "length")

    g.add_linear("m", "cm", scale=100.0)
    g.add_linear("cm", "mm", scale=10.0)
    g.add_linear("mi", "km", scale=1.60934)

    return g


@pytest.fixture()
def convert_value(unit_registry):
    def _convert(from_value, from_unit, to_unit) -> float:
        from_quantity = Quantity(from_value, from_unit)
        to_quantity = unit_registry.convert(from_quantity, to_unit)
        return to_quantity.value

    return _convert


@pytest.mark.parametrize(
    "from_value, from_unit, expected_to_value, to_unit",
    [
        (1, "m", 1000, "mm"),
        (0.5, "m", 500, "mm"),
        (2.5, "m", 2500, "mm"),
    ]
)
def test_conversions_calculation(
        unit_registry,
        from_value, from_unit, expected_to_value, to_unit,
        convert_value,
):
    to_value = convert_value(from_value, from_unit, to_unit)
    assert to_value == pytest.approx(expected_to_value)


def test_conversion_unknown_units_fails(unit_registry, convert_value):
    from_value = 1
    from_unit = "unknown_unit"
    to_unit = "mm"

    with pytest.raises(KeyError):
        convert_value(from_value, from_unit, to_unit)


def test_conversion_no_conv_path_fails(unit_registry, convert_value):
    from_value = 1
    from_unit = "mi"
    to_unit = "mm"

    with pytest.raises(ValueError):
        convert_value(from_value, from_unit, to_unit)
