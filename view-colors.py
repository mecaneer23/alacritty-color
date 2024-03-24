#!/usr/bin/env python3
# pylint: disable=invalid-name
"""
Show each regular and bold color in the current color scheme
"""

from typing import Iterable


def generate_color_blocks() -> Iterable[str]:
    """Generate a list of color blocks using ANSI"""
    for color, name in enumerate(
        (
            "Black",
            "Red",
            "Green",
            "Yellow",
            "Blue",
            "Magenta",
            "Cyan",
            "White",
        )
    ):
        yield f"{name.ljust(10)}\033[0;3{color}m█████ \033[1;3{color}m█████\033[0m"


if __name__ == "__main__":
    print("\n".join(generate_color_blocks()))
