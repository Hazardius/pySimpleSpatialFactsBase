#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pssfb. """

from sqlite3 import dbapi2 as sqlite

from pygraph.classes.digraph import digraph
from pygraph.readwrite.markup-module import markup

from pssfb_files import open_file, save_file
from pssfb_spacial_object import spacial_object

class SimpleSpatialFactsBase(object):

    def __init__(self, filename):
        try:
            self.graph = markup.read(open_file(filename))
        except:
            self.graph = digraph()

    def __del__(self):
        save_file(markup.write(self.graph))

    def inject_facts(self, facts, purge=False):
        """
        Adds facts from list facts to the base.
        If purge is set on True,
        before adding facts base should be cleaned.

        Facts is a list of tuples in format:
        (subject, relation, object).

        Given that these facts are experts' knowledge
        I assume that they're not duplicated.
        """
        if purge:
            self.graph = digraph()
        for fact in facts:
            self._inject_fact_(fact)

    def _inject_fact_(self, (subject, relation, t_object)):
        new_name_s = spacial_object(subject)
        if self.graph.has_node(new_name_s):
            self._check_consistency_(new_name_s)
        else:
            self.graph.add_node(new_name_s)

        new_name_o = spacial_object(t_object)
        if self.graph.has_node(new_name_o):
            self._check_consistency_(new_name_o)
        else:
            self.graph.add_node(new_name_o)

    def _check_consistency_(self, node, (subject, relation, t_object)):
        return True

if __name__ == '__main__':
    MYSSFB = SimpleSpatialFactsBase("ssfbase.xml")
    # TODO: All the things.
    # MYSSFB.inject_facts()
    print "Everything's OK."
