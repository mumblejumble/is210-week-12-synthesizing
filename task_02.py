#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 module"""


class CustomError(Exception):
    """CustomError Class"""
    def __init__(self, cause):
        """Class constructor"""
        Exception.__init__(self)
        self.cause = cause
