#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

import PSIToolkit

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

def psi_toolkit_pipe(text, l_code):
    psi = PSIToolkit.PipeRunner('lamerlemma --lang ' + l_code + ' ! simple-writer --tags lemma')
    return psi.run(text).split("\n")
