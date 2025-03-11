import pytest

from mdtt import bullet


# ======================================================================
# Fixtures
# ======================================================================
@pytest.fixture
def data_dir(request):
    return request.config.rootdir / "src" / "test" / "data"


# ======================================================================
# Tests
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


@pytest.mark.parametrize(
    ["input_file", "expected_file"],
    [
        pytest.param("asterisk_input.md", "asterisk_output.md", id="asterisk"),
        pytest.param("indent_input.md", "indent_output.md", id="indent"),
        pytest.param("dash_input.md", "dash_output.md", id="dash"),
        pytest.param("mixed_input.md", "mixed_output.md", id="mixed_indent"),
    ],
)
def test_format_bullet(data_dir, input_file, expected_file):
    input_file = data_dir / input_file
    text = input_file.read_text("utf-8")

    expected_file = data_dir / expected_file
    expected = expected_file.read_text("utf-8")
    actual = bullet.format(text)
    with open("/tmp/actual.md", "w") as stream:
        stream.write(actual)
    assert actual == expected


# def test_format_bullet_custom_width():
