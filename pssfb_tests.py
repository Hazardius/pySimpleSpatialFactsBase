#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import networkx.classes.function as nx

from pssfb_files import open_file
from __init__ import SimpleSpatialFactsBase, _lemma_
from __init__ import _parse_to_triple_ as ptt

class pssfb_tests(unittest.TestCase):

    def test_comp_number(self):
        results = SimpleSpatialFactsBase("other.json").facts_nr()
        expected = 0
        self.assertEqual(expected, results)

    def test_one_fact_addition(self):
    	base = SimpleSpatialFactsBase("test1.json")
    	base.inject_facts([("Polska", "PPI", "Warszawa")], purge=True)
        assert True

    def test_conflict_of_facts(self):
        base = SimpleSpatialFactsBase("test2.json")
        try:
           base.inject_facts([("Polska", "EQ", "Lechia"), \
               ("Polska", "DR", "Niemcy"), ("Lechia", "EQ", "Cebulaki"), \
               ("Lechia", "EQ", "Niemcy")], purge=True)
           my_dictionary = nx.get_edge_attributes(base.graph,'relation')
           # for key_rel in my_dictionary:
           #     print str(key_rel) + " " + str(my_dictionary[key_rel])
        except:
           assert False
        assert True

    # def test_of_saved_graph(self):
    #     base = SimpleSpatialFactsBase("test3.json")
    #     my_dictionary = nx.get_edge_attributes(base.graph,'relation')
    #     second = dict()
    #     for (key, val) in my_dictionary.iteritems():
    #         second[str(key)] = val
    #     expected = {'(cebula//0, lechia//0)': "set(['EQ'])", '(polski//0, niemie//0)': \
    #         "set(['DR'])", '(niemie//0, polski//0)': "set(['DR'])", '(lechia//0, niemie//1)': \
    #         "set(['EQ'])", '(lechia//0, cebula//0)': "set(['EQ'])", '(lechia//0, polski//0)': \
    #         "set(['EQ'])", '(polski//0, lechia//0)': "set(['EQ'])", '(niemie//1, lechia//0)': \
    #         "set(['EQ'])"}
    #     self.assertEqual(expected, second)

    # def test_inject_from_file(self):
    #     base = SimpleSpatialFactsBase("test_data.json")
    #     base._purge_()
    #     with open("test_data.txt") as text_file:
    #         for line in text_file:
    #             parts = line.split("@|@")
    #             first_name = _lemma_(parts[0])
    #             second_name = _lemma_(parts[2])
    #             if len(first_name) != 0 and len(second_name) != 0:
    #                 base.inject_facts([(first_name, parts[1], second_name)])
    #     my_dictionary = nx.get_edge_attributes(base.graph,'relation')
    #     second = dict()
    #     for (key, val) in my_dictionary.iteritems():
    #         second[str(key)] = val
    #     expected = {'(wisl//0, polski//2)': set(['PP']), '(gal//0, niec//0)': set(['EQ']), \
    #         '(polski//2, wisl//0)': set(['PPI']), '(woje//0, wisl//0)': set(['PO']), \
    #         '(polski//0, pols//0)': set(['PPI']), '(niec//0, gal//0)': set(['EQ']), \
    #         '(gdan//0, troj//0)': set(['PP']), '(wisl//0, woje//0)': set(['PO']), \
    #         '(troj//0, sopo//0)': set(['PPI']), '(troj//0, wisl//0)': set(['PO']), \
    #         '(star//0, woje//0)': set(['PP']), '(woje//0, star//0)': set(['PPI']), \
    #         '(sopo//0, troj//0)': set(['PP']), '(star//0, szcz//0)': set(['PPI']), \
    #         '(pols//0, polski//0)': set(['PP']), '(grac//0, szcz//0)': set(['DR']), \
    #         '(szcz//0, niec//0)': set(['DR']), '(star//1, grac//0)': set(['PPI']), \
    #         '(troj//0, gdan//0)': set(['PPI']), '(niec//0, szcz//0)': set(['DR']), \
    #         '(trze//0, gal//0)': set(['PPI']), '(wisl//0, troj//0)': set(['PO']), \
    #         '(szcz//0, grac//0)': set(['DR']), '(woje//0, polski//1)': set(['PP']), \
    #         '(pols//0, woje//0)': set(['PPI']), '(woje//0, pols//0)': set(['PPI']), \
    #         '(gal//0, trze//0)': set(['PP']), '(polski//1, woje//0)': set(['PPI']), \
    #         '(grac//0, star//1)': set(['PP']), '(szcz//0, star//0)': set(['PP'])}
    #     self.assertEqual(expected, second)

    def test_question_parsing(self):
        results = ptt("Czy Lechia to część Polski?")
        # Pomijanie <=3 np.
        expected = ('lechia', set(['PP']), 'polski')
        self.assertEqual(expected, results)
        results = ptt("Czy Niemcy to Polska?")
        # Pomijanie <=3 np.
        expected = ('niemiec', set(['EQ']), 'polski')
        self.assertEqual(expected, results)
        results = ptt("Czy Lechia to część Polski?")
        # Pomijanie <=3 np.
        expected = "lech@|@PP@|@polski"
        self.assertEqual(expected, results)
        results = ptt("Czy Lechia to część Polski?")
        # Pomijanie <=3 np.
        expected = "lech@|@PP@|@polski"
        self.assertEqual(expected, results)
        results = ptt("Czy Lechia to część Polski?")
        # Pomijanie <=3 np.
        expected = "lech@|@PP@|@polski"
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
