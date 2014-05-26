#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pssfb. """

import sys

import networkx as nx
from networkx.readwrite import json_graph

from pssfb_additional import polish_signs_remove as _psr_
from pssfb_files import open_file, save_file, psi_toolkit_pipe
from pssfb_spacial_fact import _compose_ as _comp_rel_
from pssfb_spacial_object import spacial_object

STEM_VALUE = 4
EQ_WORDSET = set(["jest równy"])
DR_WORDSET = set(["nie jest"])
PO_WORDSET = set(["płynie przez"])
PP_WORDSET = set(["jest częścią", "częścią"])
PPI_WORDSET = set(["zawiera"])

class SimpleSpatialFactsBase(object):

    def __init__(self, filename):
        self.filename = filename
        try:
            self.graph = nx.read_edgelist(filename, nodetype=spacial_object, \
                create_using=nx.DiGraph(), data=(('relation',str),), \
                delimiter="@|@")
        except:
            self.graph = nx.DiGraph()

    def __del__(self):
        if self.graph.edges() == []:
            nx.write_edgelist(self.graph, self.filename, data=["relation"], \
                delimiter="@|@")

    def facts_nr(self):
        return nx.classes.function.number_of_edges(self.graph)

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
            self.graph = nx.DiGraph()
        for fact in facts:
            self._inject_fact_(fact)

    def check_fact(self, line):
        (first_name, relation, second_name) = _parse_to_triple_(line)
        if len(first_name) > 0 and len(second_name) > 0:
            answer = self._check_fact_(first_name, relation, second_name)
            return answer
        else:
            return "ERROR"

    def _check_fact_(self, first_name, relation, second_name):
        if self._confirmation_(first_name, second_name, relation):
            return "True"
        elif self._falsification_(first_name, second_name, relation):
            return "False"
        return "Unknown"

    def _confirmation_(self, from_n, to_n, relation):
        new_name_s = spacial_object(from_n, 0)
        while new_name_s in self.graph:
            new_name_o = spacial_object(to_n, 0)
            while new_name_o in self.graph:
                # print str(new_name_s) + " -> " + str(new_name_o) + " :"
                if self._check_consistency_(new_name_s, new_name_o, relation):
                    return True
                new_name_o.o_nr += 1
            new_name_s.o_nr += 1
        return False

    def _falsification_(self, from_n, to_n, relation):
        new_name_s = spacial_object(from_n, 0)
        while new_name_s in self.graph:
            new_name_o = spacial_object(to_n, 0)
            while new_name_o in self.graph:
                if self._check_consistency_fals_(new_name_s, new_name_o, relation) == False:
                    return True
                new_name_o.o_nr += 1
            new_name_s.o_nr += 1
        return False

    def _purge_(self):
        self.graph = nx.DiGraph()

    def _inject_fact_(self, (subject, relation, t_object)):
        subject = _lemma_(subject)
        t_object = _lemma_(t_object)

        new_name_s = spacial_object(subject, 0)
        if not new_name_s in self.graph:
            self.graph.add_node(new_name_s)

        new_name_o = spacial_object(t_object, 0)
        end = False
        new_name_o.o_nr -= 1
        while end == False:
            new_name_o.o_nr += 1
            end = self._consistency_run_(new_name_s, new_name_o, relation)

    def _consistency_run_(self, sub, obj, rel):
        if obj not in self.graph:
            self.graph.add_node(obj)
            self.graph.add_edge(sub, obj, relation=set([rel]))
            self.graph.add_edge(obj, sub, relation=set([_bin_rel_(rel)]))
            return True
        elif self._check_consistency_(sub, obj, rel):
            self.graph.add_node(obj)
            self.graph.add_edge(sub, obj, relation=set([rel]))
            self.graph.add_edge(obj, sub, relation=set([_bin_rel_(rel)]))
            return True
        return False

    def _check_consistency_fals_(self, my_start, my_node, relation):
        if nx.algorithms.shortest_paths.generic.has_path(self.graph, my_start, my_node):
            # print "Z " + str(my_start)
            # print "Do " + str(my_node)
            path = nx.algorithms.shortest_paths.unweighted.predecessor( \
                self.graph, my_start)
            pred_rel = self._predicted_relation_(path, my_start, my_node)
            if relation not in pred_rel:
                return False
        return True

    def _check_consistency_(self, my_start, my_node, relation):
        # print str(my_start) + " -" + relation + "-> " + str(my_node)
        if my_node in self.graph: #G:
            if nx.algorithms.shortest_paths.generic.has_path(self.graph, my_start, my_node):
                # print "Z " + str(my_start)
                # print "Do " + str(my_node)
                path = nx.algorithms.shortest_paths.unweighted.predecessor( \
                    self.graph, my_start)
                # print "Path " + str(path)
                pred_rel = self._predicted_relation_(path, my_start, my_node)
                # print "Pred_rel " + str(pred_rel)
                if pred_rel != set([relation]):
                    return False
        return True

    def _predicted_relation_(self, path, start, target):
        current = target
        relation = set(["EQ"])
        while current != start:
            next = path[current][0]
            next_rel = self.graph.edge[next][current]["relation"]
            current = next
            # print str(next_rel) + " (X) " + str(relation)
            relation = _comp_rel_(next_rel, relation)
            # print str(next) + " -> " + str(target) + " " + str(relation)
        return relation

def _bin_rel_(relation):
    if relation == "PP":
        return "PPI"
    elif relation == "PPI":
        return "PP"
    return relation

def _lemma_(entity):
    form_ent = entity.lower()
    form_ent_tab = form_ent.split()
    table = []
    # DEBUG prints
    # print "ent: " + str(form_ent)
    # print "tab: " + str(form_ent_tab)
    for iterat in range(len(form_ent_tab)):
        try_lem = psi_toolkit_pipe(form_ent_tab[iterat], "pl")[0]
        if len(try_lem) == 0:
            table += [_psr_(form_ent_tab[iterat])[:STEM_VALUE]]
        elif "|" in try_lem:
            table += [_psr_(try_lem.split("|")[0])]
        else:
            table += [_psr_(try_lem)]
    str_lem = '_'.join(table)
    # print "stl: " + str_lem
    return str_lem

def _parse_to_triple_(question):
    # Question without "Czy " and "?"
    question = question.lower()
    if question[-1] == "?":
        question = question[:-1]
    question = question.replace("to część", "częścią")
    question = question.replace("to", "jest równy")
    imp_wds = [word for word in question.split() if (len(word)>3)]
    if len(imp_wds) == 3:
        return (imp_wds[0], to_rel(imp_wds[1]), imp_wds[2])
    #relacja = _find_rel_(imp_wds)
    return (imp_wds[0], to_rel(imp_wds[1]), imp_wds[2])

# TODO: For each keyword known in WORDSET try to search in sentence
# Then add first match
def to_rel(word):
    ret_val = set()
    if word in EQ_WORDSET:
        ret_val.add("EQ")
    if word in DR_WORDSET:
        ret_val.add("DR")
    if word in PP_WORDSET:
        ret_val.add("PP")
    if word in PPI_WORDSET:
        ret_val.add("PPI")
    if word in PO_WORDSET:
        ret_val.add("PO")
    return ret_val


# Main function works with polish question "Czy (...)?"
if __name__ == '__main__':
    MYSSFB = SimpleSpatialFactsBase("ssfbase.json")
    try:
        work_type = sys.argv[1][1]
        if work_type == "f":
            for line in sys.stdin:
                parts = line.split("@|@")
                MYSSFB.inject_facts([(parts[0], parts[1], parts[2])])
                print "\"" + str((parts[0], set([parts[1]]), parts[2])) + "\" added."
            print "Time for the end."
        elif work_type == "a":
            for line in sys.stdin:
                answer = MYSSFB.check_fact(line[:-1])
                print line[:-1] + " @|@ " + answer
            print "Time for the end."
    except:
        print "Unknown argument!"
