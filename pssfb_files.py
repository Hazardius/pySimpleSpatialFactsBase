#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

""" This file contains logic of file IN/OUT operations. """

def open_file(path):
    """ Opening a file specified by a path. """
    with open(path) as f_in:
        return f_in

def save_file(path, content):
    """ Saving output to the specified path."""
    f = codecs.open(path, "w", "utf-8")
    f.write(content)
    f.close()
