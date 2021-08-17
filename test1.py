#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020-04-06 12:33
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

# 断言异常
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
        # 详细断言异常
def test_zero_division_long():
            with pytest.raises(ZeroDivisionError) as excinfo:
                1 / 0

            # 断言异常类型 type
            assert excinfo.type == ZeroDivisionError
            # 断言异常 value 值
            assert "division by zero" in str(excinfo.value)