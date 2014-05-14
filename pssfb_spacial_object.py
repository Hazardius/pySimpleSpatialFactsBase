#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial object definition. """

import sqlite3

class spacial_object(object):
    o_name = None
    # Unused
    # o_type = None
    o_nr = None
    o_comp = None

    def __init__(self, name, nr, comp):
    # Unused
    # def __init__(self, name, type_str, nr):
        """Constructor."""
        self.o_name = name
        # Unused
        # self.o_type = type_str
        self.o_nr = nr
        self.o_comp = comp

    def __repr__(self):
        return self.o_name + "/" + str(self.o_nr) + "/" + str(self.o_comp)
        # Unused
        # return self.o_name + "/" + self.o_type + "/" + str(self.o_nr) + "/" + str(self.o_comp)

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%f" % (self.x, self.y)
