#!/usr/bin/env python3
"""Type annotated floor function"""


def floor(n: float) -> int:
    """Return the floor of a floating point number"""
    if n < 0 and n != int(n):
        return int(n - 1)
    return int(n)
