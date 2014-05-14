#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" File containing simple spacial fact definition. """

from pssfb_additional import enum

# RCC5
# DR - disconnected
# PO - partially overlapping
# PP - proper part
# PPI - proper part inversed
# EQ - equal
rel_type = enum(DR = "DR", PO = "PO", PP = "PP", PPI = "PPI", EQ = "EQ")
ALL_RELATIONS = set([rel_type.DR, rel_type.PO, rel_type.PP, rel_type.PPI, rel_type.EQ])

class spacial_fact(object):
    f_subject = None
    f_object = None
    f_relation = None

    def __init__(self, sub, rel, obj):
        """Constructor."""
        self.f_subject = sub
        self.f_object = obj
        if type(rel) is type(set()):
            self.f_relation = set() | rel
        else:
            self.f_relation = set()
            self.f_relation.add(rel)

    def __repr__(self):
        return str(self.f_subject) + " " + str(self.f_relation) + " " + str(self.f_object)

    def get_id(self):
        return str(self.f_subject) + " " + str(self.f_relation).replace("', '", ",").replace("set(['", "--").replace("'])", "->") + " " + str(self.f_object)

    def compose(self, second_fact):
        if str(self.f_object) == str(second_fact.f_subject):
            new_rel = set()
            for one_fr_rel in self.f_relation:
                if new_rel == ALL_RELATIONS:
                    break;
                for one_to_rel in second_fact.f_relation:
                    new_rel = new_rel | _compose_relations_(one_fr_rel, one_to_rel)
            return spacial_fact(self.f_subject, new_rel, second_fact.f_object)
        else:
            # Tried to compose facts without common part!
            return None

def _compose_relations_(prev_rel, next_rel):
    """ Typical for RCC5. """
    if next_rel == rel_type.EQ:
        return set([prev_rel])
    elif prev_rel == rel_type.EQ:
        return set([next_rel])
    elif next_rel == rel_type.PPI:
        if prev_rel == rel_type.PP:
            return ALL_RELATIONS
        elif prev_rel == rel_type.PO:
            return set([rel_type.DR, rel_type.PO, rel_type.PPI])
        elif prev_rel == rel_type.DR:
            return set([prev_rel])
        else:
            return next_rel
    elif next_rel == rel_type.PP:
        if prev_rel == rel_type.DR:
            return set([rel_type.DR, rel_type.PO, rel_type.PP])
        elif prev_rel == rel_type.PO:
            return set([rel_type.PO, rel_type.PP])
        elif prev_rel == rel_type.PPI:
            return set([rel_type.PO, rel_type.PP, rel_type.PPI, rel_type.EQ])
        else:
            return set([next_rel])
    elif next_rel == rel_type.PO:
        if prev_rel == rel_type.PO:
            return ALL_RELATIONS
        elif prev_rel == rel_type.PPI:
            return set([rel_type.PO, rel_type.PPI])
        else:
            return set([rel_type.DR, rel_type.PO, rel_type.PP])
    else:
        if prev_rel == rel_type.DR:
            return ALL_RELATIONS
        elif prev_rel == rel_type.PP:
            return set([next_rel])
        else:
            return set([rel_type.DR, rel_type.PO, rel_type.PPI])
