import io
import re
import textwrap


def get_indentation(text: str):
    bullet_pattern = re.compile("^( *[*-] *)")
    if match := bullet_pattern.search(text):
        return match[1], " " * len(match[1])
    return "- ", "  "


def _collect(buffer: io.StringIO, seq: list, width: int, indent: str):
    bullet = buffer.getvalue()
    if not bullet:
        return

    seq.append(
        textwrap.fill(
            text=bullet,
            width=width,
            subsequent_indent=indent,
        )
    )
    buffer.seek(0)
    buffer.truncate()


def format(text: str, width=72):
    bullets = []
    collected = io.StringIO()
    indent = ""

    for line in text.splitlines():
        trimmed = line.strip()
        if trimmed.startswith(("- ", "* ")):
            _collect(collected, bullets, width, indent)
            _, indent = get_indentation(line)
        collected.write(f"{line}\n")

    # Is there any left over?
    _collect(collected, bullets, width, indent)

    return "\n".join(bullets)
