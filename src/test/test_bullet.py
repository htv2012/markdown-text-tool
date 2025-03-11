import pytest

from mdtt import bullet


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
    ],
)
def test_format_bullet(request, input_file, expected_file):
    print(f"{request.config.rootdir=}")
    input_file = request.config.rootdir / "src" / "test" / "data" / input_file
    print(f"{input_file=}")
    text = input_file.read_text("utf-8")

    expected_file = request.config.rootdir / "src" / "test" / "data" / expected_file
    expected = expected_file.read_text("utf-8")
    actual = bullet.format(text)
    assert actual == expected
