#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 module"""


class BaseError(Exception):
    """BaseError Class"""
    pass


class StringError(BaseError, TypeError):
    """StringError Class"""
    pass


class NumberError(BaseError, TypeError):
    """NumberError Class"""
    pass


class NonZeroError(NumberError):
    """NonZeroError Class"""
    pass
