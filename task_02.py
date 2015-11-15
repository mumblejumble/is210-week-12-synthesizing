#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 module"""


class CustomError(Exception):
    """CustomError Class

    Attributes:
        Exception(class): subclassing from Exception class.
        cause(string): a string
    """

    def __init__(self, msg, cause):
        """Exception class constructor

        Args:
            msg(str): msg of the exception.
            cause(str): cause of exception.

        Attributes:
            msg(str): msg of the exception.
            cause(str): cause of exception.
        """
        Exception.__init__(self)
        self.msg = msg
        self.cause = cause
