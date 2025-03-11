import io
import re
import textwrap


def get_indentation(text: str):
    bullet_pattern = re.compile("^( *[*-] *)")
    if match := bullet_pattern.search(text):
        return match[1], " " * len(match[1])
    return "- ", "  "


def format(text: str, width=72):
    initial_indent, subsequent_indent = get_indentation(text)
    buf = io.StringIO()
    separator = re.compile(r"^ *[*-] +", re.MULTILINE)
    bullets = separator.split(text)
    print(f"{initial_indent=}")

    for bullet in bullets:
        bullet = textwrap.fill(
            bullet,
            width=width,
            initial_indent=initial_indent,
            subsequent_indent=subsequent_indent,
        )
        buf.write(bullet)
        buf.write("\n")

    return buf.getvalue()
