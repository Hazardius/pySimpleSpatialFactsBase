#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial object definition. """

class spacial_object(object):
    o_name = None
    o_type = None
    o_nr = None

    def __init__(self, name, type_str, nr):
        """Constructor."""
        self.o_name = name
        self.o_type = type_str
        self.o_nr = nr

    def __repr__(self):
        return self.o_name + "/" + self.o_type + "/" + str(self.o_nr)
