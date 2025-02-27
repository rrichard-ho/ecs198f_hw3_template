import pytest

def foo_bar_baz(n: int) -> str:
    return_str = ""
    for i in range(1, n + 1, 1):
        if (i % 3 == 0) and (i % 5 == 0):
            return_str += "Baz"
        elif i % 3 == 0:
            return_str += "Foo"
        elif i % 5 == 0:
            return_str += "Bar"
        else:
            return_str += str(i)
        if i < n:
            return_str += " "
    return return_str

def test_foo_bar_baz():
    assert foo_bar_baz(1) == "1"

    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

    assert foo_bar_baz(-1) == ""

    assert foo_bar_baz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"