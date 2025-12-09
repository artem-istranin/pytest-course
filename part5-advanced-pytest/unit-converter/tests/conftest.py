import pytest

from uc.converter import ConversionGraph


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
