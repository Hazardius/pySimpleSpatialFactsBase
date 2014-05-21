#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#import networkx.classes.function as nx

from __init__ import SimpleSpatialFactsBase
from __init__ import _parse_to_triple_ as ptt

class pssfb_tests(unittest.TestCase):

    #def test_comp_number(self):
    #    results = SimpleSpatialFactsBase("other.json").facts_nr()
    #    expected = 0
    #    self.assertEqual(expected, results)

    #def test_one_fact_addition(self):
    # 	base = SimpleSpatialFactsBase("test1.json")
    # 	base.inject_facts([("Polska", "PPI", "Warszawa")], purge=True)

    #def test_conflict_of_facts(self):
    #    base = SimpleSpatialFactsBase("test2.json")
    #    try:
    #        base.inject_facts([("Polska", "EQ", "Lechia"), \
    #            ("Polska", "DR", "Niemcy"), ("Lechia", "EQ", "Cebulaki"), \
    #            ("Lechia", "EQ", "Niemcy")], purge=True)
    #        my_dictionary = nx.get_edge_attributes(base.graph,'relation')
    #        for key_rel in my_dictionary:
    #            print str(key_rel) + " " + str(my_dictionary[key_rel])
    #    except:
    #        assert False

    # def test_of_saved_graph(self):
    #     base = SimpleSpatialFactsBase("test3.json")
    #     my_dictionary = nx.get_edge_attributes(base.graph,'relation')
    #     for key_rel in my_dictionary:
    #         print str(key_rel) + " " + str(my_dictionary[key_rel])

    def test_question_parsing(self):
        results = ptt("Czy Lechia to część Polski?")
        # Pomijanie <=3 np.
        expected = "Lechia@|@PP@|@Polska"
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
