#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlite3 import dbapi2 as sqlite

""" Main file of pssfb. """

class SimpleSpatialFactsBase(object):

    def __init__(self, db_name):
        self.db = sqlite.connect(db_name)

    def __del__(self):
        self.db.close()

    def inject_facts(self, facts, purge=False):
        """
        Adds facts from list facts to the base.
        If purge is set on True,
        before adding facts base should be cleaned.
        """
        if purge:
            self._purge_()
        for fact in facts:
            if not fact.get_id() in self.fact_db:
                self.fact_db[fact.get_id] = fact

    def _purge_(self):
        self.db.execute("delete from facts")
        self.db.execute("delete from components")

    def get_comp_nr(self):
        cursor = self.db.execute("select count(*) from components")
        result = cursor.fetchone()
        return result[0]

if __name__ == '__main__':
    MYSSFB = SimpleSpatialFactsBase("ssfbase.db")
    # TODO: All the things.
    # MYSSFB.inject_facts()
    print "Everything's OK."
