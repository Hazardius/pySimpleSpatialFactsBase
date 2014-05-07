#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve

""" Main file of pssfb. """

class SimpleSpatialFactsBase(object):
    def __init__(self, dbname):
        self.link_db = shelve.open(dbname)

    def __del__(self):
        self.link_db.close()

    def inject_facts(self, facts, purge=False):
        """
        Adds facts from list facts to the base.
        If purge is set on True,
        before adding facts base should be cleaned.
        """
        # TODO: Think about how to use facts to answer questions.
        if purge:
            self.link_db.clear()
        for fact in facts:
            if not fact.get_id() in self.link_db:
                self.link_db[fact.get_id] = fact

if __name__ == '__main__':
    MYSSFB = SimpleSpatialFactsBase("facts.db")
    # TODO: All the things.
    # MYSSFB.inject_facts()
    print "Everything's OK."
