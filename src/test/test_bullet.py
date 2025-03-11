import pathlib

import pytest

from mdtt import bullet


@pytest.mark.parametrize(
    ["text", "expected"],
    [
        pytest.param("- bullet1\n- bullet2", ("- ", "  "), id="no indent"),
        pytest.param("    - bullet", ("    - ", "      "), id="indent 4 columns"),
    ],
)
def test_indentation(text, expected):
    assert bullet.get_indentation(text) == expected


@pytest.mark.parametrize(
    ["text", "expected"],
    [
        pytest.param(
            "    * Lorem ipsum odor amet, consectetuer adipiscing elit.\n"
            "Fames vulputate - iaculis magna malesuada dignissim elementum ut maximus.\n"
            "    * Magna habitant mi auctor facilisis\n"
            "urna nullam sapien. Curae donec mauris maximus morbi\n"
            "porttitor mus per auctor pretium.\n"
            "    * Lacus ultrices congue pellentesque vel tempor convallis egestas. Faucibus aliquam risus diam faucibus; sit etiam ad hac.\n"
            "    * Pellentesque praesent scelerisque sit litora class ultrices phasellus luctus. Semper quis eleifend quam morbi non hendrerit condimentum euismod.",
            "    * Lorem ipsum odor amet, consectetuer adipiscing elit. Fames\n"
            "      vulputate - iaculis magna malesuada dignissim elementum ut\n"
            "      maximus.\n"
            "    * Magna habitant mi auctor facilisis urna nullam sapien. Curae donec\n"
            "      mauris maximus morbi porttitor mus per auctor pretium.\n"
            "    * Lacus ultrices congue pellentesque vel tempor convallis egestas.\n"
            "      Faucibus aliquam risus diam faucibus; sit etiam ad hac.\n"
            "    * Pellentesque praesent scelerisque sit litora class ultrices\n"
            "      phasellus luctus. Semper quis eleifend quam morbi non hendrerit\n"
            "      condimentum euismod.\n",
            id="no indent",
        ),
    ],
)
def test_format_bullet(text, expected):
    actual = bullet.format(text)
    pathlib.Path("/tmp/in.md").write_text(text)
    pathlib.Path("/tmp/actual.md").write_text(actual)
    pathlib.Path("/tmp/expected.md").write_text(expected)
    assert actual == expected
