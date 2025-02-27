import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def test_normal():
    assert foo_bar_baz(1) == "1"

    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

def test_negative():
    assert foo_bar_baz(-1) == ""

def test_large():
    assert foo_bar_baz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"