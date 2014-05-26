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
    	base.inject_facts([("Wielki Mur Chiński", "PP", "Chińska Republika Ludowa")], \
            purge=True)
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

    def test_of_saved_graph(self):
        base = SimpleSpatialFactsBase("test3.json")
        my_dictionary = nx.get_edge_attributes(base.graph,'relation')
        second = dict()
        for (key, val) in my_dictionary.iteritems():
            second[str(key)] = val
        expected = {'(cebula//0, lechia//0)': set(['EQ']), '(polski//0, niemie//0)': \
            set(['DR']), '(niemie//0, polski//0)': set(['DR']), '(lechia//0, niemie//1)': \
            set(['EQ']), '(lechia//0, cebula//0)': set(['EQ']), '(lechia//0, polski//0)': \
            set(['EQ']), '(polski//0, lechia//0)': set(['EQ']), '(niemie//1, lechia//0)': \
            set(['EQ'])}
        self.assertEqual(expected, second)

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
        expected = {
            '(szczuczyn//0, grajewo//0)': set(['DR']), \
            '(grajewo//0, szczuczyn//0)': set(['DR']), \
            '(starostwo_grajewo//1, grajewo//0)': set(['PPI']), \
            '(starostwo_grajewo//0, wojewodztwo_podlaski//0)': set(['PP']), \
            '(trojmiasto//0, wisla//0)': set(['PO']), \
            '(szczuczyn//0, starostwo_grajewo//0)': set(['PP']), \
            '(wojewodztwo_wielkopolski//0, polska//0)': set(['PP']), \
            '(trzeci_rzesza//0, gali//0)': set(['PPI']), \
            '(sopot//0, trojmiasto//0)': set(['PP']), \
            '(szczuczyn//0, niec//0)': set(['DR']), \
            '(grajewo//0, starostwo_grajewo//1)': set(['PP']), \
            '(polska//0, wisla//0)': set(['PPI']), \
            '(wojewodztwo_mazowiecki//0, wisla//0)': set(['PO']), \
            '(gali//0, trzeci_rzesza//0)': set(['PP']), \
            '(gdansk//0, trojmiasto//0)': set(['PP']), \
            '(polska//0, polska_b//0)': set(['PPI']), \
            '(wisla//0, wojewodztwo_malopolski//0)': set(['PO']), \
            '(polska//0, wojewodztwo_wielkopolski//0)': set(['PPI']), \
            '(wisla//0, trojmiasto//0)': set(['PO']), \
            '(wojewodztwo_malopolski//0, wisla//0)': set(['PO']), \
            '(polska_b//0, polska//0)': set(['PP']), \
            '(starostwo_grajewo//0, szczuczyn//0)': set(['PPI']), \
            '(gali//0, niec//0)': set(['EQ']), \
            '(niec//0, gali//0)': set(['EQ']), \
            '(wojewodztwo_podlaski//0, starostwo_grajewo//0)': set(['PPI']), \
            '(wisla//0, polska//0)': set(['PP']), \
            '(trojmiasto//0, sopot//0)': set(['PPI']), \
            '(trojmiasto//0, gdansk//0)': set(['PPI']), \
            '(polska_b//0, wojewodztwo_podlaski//0)': set(['PPI']), \
            '(niec//0, szczuczyn//0)': set(['DR']), \
            '(wojewodztwo_podlaski//0, polska_b//0)': set(['PP']), \
            '(wisla//0, wojewodztwo_mazowiecki//0)': set(['PO'])
        }

        self.assertEqual(expected, second)

        # Start of asking questions
        # answer = base._check_fact_("szczuczyn", "EQ", "grajewo")
        # # print "szcz EQ graj -> " + answer
        # self.assertEqual("False", answer)
        # answer = base._check_fact_("polska", "EQ", "trzeci_rzesza")
        # # print "polski EQ trzeci_rzesza -> " + answer
        # self.assertEqual("Unknown", answer)
        # answer = base._check_fact_("szczuczyn", "PP", "polska")
        # # print "szcz PP polski -> " + answer
        # self.assertEqual("True", answer)
        # answer = base._check_fact_("niec", "PP", "trzeci_rzesza")
        # # print "niec PP trzeci_rzesza -> " + answer
        # self.assertEqual("True", answer)
        # answer = base._check_fact_("trojmiasto", "DR", "polska")
        # # print "trojmiasto DR polski -> " + answer
        # self.assertEqual("False", answer)
        # answer = base._check_fact_("gdansk", "PP", "polska")
        # # print "gdan PP polski -> " + answer
        # self.assertEqual("Unknown", answer)

        answer = base.check_fact("Czy Szczuczyn jest Grajewem?")
        self.assertEqual("False", answer)
        answer = base.check_fact("Czy Trójmiasto nie jest Polską?")
        self.assertEqual("False", answer)
        answer = base.check_fact("Czy Szczuczyn leży w Polsce?")
        self.assertEqual("True", answer)
        answer = base.check_fact("Czy Niećkowo jest częścią Trzeciej Rzeszy?")
        self.assertEqual("True", answer)
        answer = base.check_fact("Czy Polska jest Trzecią Rzeszą?")
        self.assertEqual("Unknown", answer)
        answer = base.check_fact("Czy Gdańsk leży w Polsce?")
        self.assertEqual("Unknown", answer)

    def test_questions_to_saved_graph(self):
        base = SimpleSpatialFactsBase("test_data.json")
        base.filename = "dump.json"
        answer = base.check_fact("Czy Szczuczyn jest Grajewem?")
        self.assertEqual("False", answer)
        answer = base.check_fact("Czy Trójmiasto nie jest Polską?")
        self.assertEqual("False", answer)
        answer = base.check_fact("Czy Szczuczyn leży w Polsce?")
        self.assertEqual("True", answer)
        answer = base.check_fact("Czy Niećkowo jest częścią Trzeciej Rzeszy?")
        self.assertEqual("True", answer)
        answer = base.check_fact("Czy Polska jest Trzecią Rzeszą?")
        self.assertEqual("Unknown", answer)
        answer = base.check_fact("Czy Gdańsk leży w Polsce?")
        self.assertEqual("Unknown", answer)

    def test_question_parsing(self):
        results = ptt("Czy Polska zawiera Szczuczyn?")
        expected = ('polska', 'PPI', 'szczuczyn')
        self.assertEqual(expected, results)

        results = ptt("Czy Niemcy to Polska?")
        expected = ('niemcy', 'EQ', 'polska')
        self.assertEqual(expected, results)

        results = ptt("Czy Wisła płynie przez Polskę?")
        expected = ('wisla', 'PO', 'polska')
        self.assertEqual(expected, results)

        results = ptt("Czy Polska nie jest Trzecią Rzeszą?")
        expected = ('polska', 'DR', 'trzeci_rzesza')
        self.assertEqual(expected, results)

        results = ptt("Czy Polska B jest częścią Polski?")
        expected = ('polska_b', 'PP', 'polska')
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
