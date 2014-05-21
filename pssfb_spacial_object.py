#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial object definition. """

class spacial_object(object):
    o_name = None
    o_nr = None

    def __init__(self, *args, **kwargs):
        """Constructor."""
        if len(args) == 2:
            self.o_name = args[0]
            self.o_nr = args[1]
        else:
            splitted = args[0].split("//")
            self.o_name = splitted[0]
            if len(splitted) == 1:
                self.o_nr = 0
            else:
                self.o_nr = int(splitted[1])

    def __repr__(self):
        return str(self.o_name) + "//" + str(self.o_nr)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False
