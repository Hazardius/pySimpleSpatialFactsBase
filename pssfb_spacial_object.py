#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial object definition. """

class spacial_object(object):
    o_name = None
    o_nr = None

    def __init__(self, name, nr=0):
        """Constructor."""
        self.o_name = name
        self.o_nr = nr

    def __repr__(self):
        return self.o_name + "/" + str(self.o_nr)
