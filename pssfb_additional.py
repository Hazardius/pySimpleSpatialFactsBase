#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Additional tools used by pssfb. """

def enum(**enums):
    return type('Enum', (), enums)

