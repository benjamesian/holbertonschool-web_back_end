#!/usr/bin/env python3
"""Type annotated floor function"""


def floor(n: float) -> int:
    """Return the floor of a floating point number"""
    return int(n) if n >= 0 else int(n - 1)
