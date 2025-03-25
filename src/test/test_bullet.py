import types

import pytest

from mdtt import bullet

# ======================================================================


@pytest.fixture
def data_dir(request):
    return request.config.rootdir / "src" / "test" / "data"


# ======================================================================


@pytest.mark.parametrize(
    ["text", "expected"],
    [
        pytest.param("* bullet1\n* bullet2", ("* ", "  "), id="asterisk"),
        pytest.param("- bullet1\n- bullet2", ("- ", "  "), id="dash"),
        pytest.param("    - bullet", ("    - ", "      "), id="indent"),
    ],
)
def test_indentation(text, expected):
    assert bullet.get_indentation(text) == expected


# ======================================================================


@pytest.fixture(
    params=[
        pytest.param(("asterisk_input.md", "asterisk_output.md", {}), id="asterisk"),
        pytest.param(("dash_input.md", "dash_output.md", {}), id="dash"),
        pytest.param(("indent_input.md", "indent_output.md", {}), id="indent"),
        pytest.param(("mixed_input.md", "mixed_output.md", {}), id="mixed"),
        pytest.param(
            ("width_input.md", "width_output.md", {"width": 65}), id="custom_width"
        ),
    ]
)
def format_data(request, data_dir):
    return types.SimpleNamespace(
        input_text=(data_dir / request.param[0]).read_text("utf-8"),
        expected=(data_dir / request.param[1]).read_text("utf-8"),
        kwargs=request.param[2],
    )


def test_format_bullet(format_data):
    actual = bullet.format(format_data.input_text, **format_data.kwargs)
    assert actual == format_data.expected
