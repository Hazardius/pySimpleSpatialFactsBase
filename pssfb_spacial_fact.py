#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial fact definition. """

# RCC5
# DR - disconnected
# PO - partially overlapping
# PP - proper part
# EQ - equal
rel_type = enum(DR = "DR", PO = "PO", PP = "PP", EQ = "EQ")

class spacial_fact(object):
    f_subject = None
    f_object = None
    f_relation = None

    def __init__(self, sub, obj, rel):
        """Constructor."""
        self.f_subject = sub
        self.f_object = obj
        self.f_relation = rel

    def __repr__(self):
        return str(f_subject) + f_relation + str(f_object)

