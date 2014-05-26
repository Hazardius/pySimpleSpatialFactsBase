#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import networkx.classes.function as nx

from pssfb_files import open_file
from __init__ import SimpleSpatialFactsBase, _lemma_
from __init__ import _parse_to_triple_ as ptt

class pssfb_tests(unittest.TestCase):

    # def test_comp_number(self):
    #     results = SimpleSpatialFactsBase("other.json").facts_nr()
    #     expected = 0
    #     self.assertEqual(expected, results)

    # def test_one_fact_addition(self):
    # 	base = SimpleSpatialFactsBase("test1.json")
    # 	base.inject_facts([("Polska", "PPI", "Warszawa")], purge=True)
    #     assert True

    # def test_conflict_of_facts(self):
    #     base = SimpleSpatialFactsBase("test2.json")
    #     try:
    #        base.inject_facts([("Polska", "EQ", "Lechia"), \
    #            ("Polska", "DR", "Niemcy"), ("Lechia", "EQ", "Cebulaki"), \
    #            ("Lechia", "EQ", "Niemcy")], purge=True)
    #        my_dictionary = nx.get_edge_attributes(base.graph,'relation')
    #        # for key_rel in my_dictionary:
    #        #     print str(key_rel) + " " + str(my_dictionary[key_rel])
    #     except:
    #        assert False
    #     assert True

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

    def test_inject_from_file_and_ask(self):
        base = SimpleSpatialFactsBase("test_data.json")
        base._purge_()
        with open("test_data.txt") as text_file:
            for line in text_file:
                parts = line.split("@|@")
                base.inject_facts([(parts[0], parts[1], parts[2])])
        my_dictionary = nx.get_edge_attributes(base.graph,'relation')
        second = dict()
        for (key, val) in my_dictionary.iteritems():
            second[str(key)] = val
        expected = {'(polski//0, wisl//0)': set(['PPI']), '(starostwo_graj//1, graj//0)': \
            set(['PPI']), '(wisl//0, wojewodztwo_mazowiecki//0)': set(['PO']), \
            '(wojewodztwo_wielkopolski//0, polski//0)': set(['PP']), '(gali//0, niec//0)': \
            set(['EQ']), '(polski_bar//0, wojewodztwo_podlaski//0)': set(['PPI']), \
            '(szcz//0, graj//0)': set(['DR']), '(polski_bar//0, polski//0)': set(['PP']), \
            '(trzeci_rzesza//0, gali//0)': set(['PPI']), '(trojmiasto//0, gdan//0)': \
            set(['PPI']), '(wisl//0, trojmiasto//0)': set(['PO']), \
            '(starostwo_graj//0, wojewodztwo_podlaski//0)': set(['PP']), \
            '(gali//0, trzeci_rzesza//0)': set(['PP']), '(szcz//0, niec//0)': set(['DR']), \
            '(wisl//0, polski//0)': set(['PP']), '(niec//0, szcz//0)': set(['DR']), \
            '(graj//0, starostwo_graj//1)': set(['PP']), '(niec//0, gali//0)': set(['EQ']), \
            '(wojewodztwo_podlaski//0, polski_bar//0)': set(['PPI']), \
            '(wisl//0, wojewodztwo_malopolski//0)': set(['PO']), '(trojmiasto//0, wisl//0)': \
            set(['PO']), '(starostwo_graj//0, szcz//0)': set(['PPI']), \
            '(polski//0, wojewodztwo_wielkopolski//0)': set(['PPI']), \
            '(wojewodztwo_podlaski//0, starostwo_graj//0)': set(['PPI']), \
            '(szcz//0, starostwo_graj//0)': set(['PP']), '(trojmiasto//0, sopo//0)': \
            set(['PPI']), '(gdan//0, trojmiasto//0)': set(['PP']), \
            '(wojewodztwo_mazowiecki//0, wisl//0)': set(['PO']), '(graj//0, szcz//0)': \
            set(['DR']), '(polski//0, polski_bar//0)': set(['PPI']), \
            '(sopo//0, trojmiasto//0)': set(['PP']), '(wojewodztwo_malopolski//0, wisl//0)': \
            set(['PO'])}

        self.assertEqual(expected, second)
        answer = base._check_fact_("polski", "EQ", "trzeci_rzesza")
        print "polski EQ trzeci_rzesza -> " + answer
        answer = base._check_fact_("szcz", "EQ", "graj")
        print "szcz EQ graj -> " + answer

        # Start of asking questions
        question1 = ("polski", "EQ", "Trzecia Rzesza")

    # def test_question_parsing(self):
    #     results = ptt("Czy Lechia to część Polski?")
    #     # Pomijanie <=3 np.
    #     expected = ('lechia', set(['PP']), 'polski')
    #     self.assertEqual(expected, results)
    #     results = ptt("Czy Niemcy to Polska?")
    #     # Pomijanie <=3 np.
    #     expected = ('niemiec', set(['EQ']), 'polski')
    #     self.assertEqual(expected, results)
    #     results = ptt("Czy Lechia to część Polski?")
    #     # Pomijanie <=3 np.
    #     expected = "lech@|@PP@|@polski"
    #     self.assertEqual(expected, results)
    #     results = ptt("Czy Lechia to część Polski?")
    #     # Pomijanie <=3 np.
    #     expected = "lech@|@PP@|@polski"
    #     self.assertEqual(expected, results)
    #     results = ptt("Czy Lechia to część Polski?")
    #     # Pomijanie <=3 np.
    #     expected = "lech@|@PP@|@polski"
    #     self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
