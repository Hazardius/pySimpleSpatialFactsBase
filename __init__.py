#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main file of pssfb. """

import sys

import networkx as nx
from networkx.readwrite import json_graph

from pssfb_files import open_file, save_file, psi_toolkit_pipe
from pssfb_spacial_fact import _compose_ as _comp_rel_
from pssfb_spacial_object import spacial_object

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

    def _inject_fact_(self, (subject, relation, t_object)):
        new_name_s = spacial_object(subject, 0)
        if not new_name_s in self.graph:
            self.graph.add_node(new_name_s)

        new_name_o = spacial_object(t_object, 0)
        end = False
        new_name_o.o_nr -= 1
        while end == False:
            new_name_o.o_nr += 1
            end = self._consistency_run_(new_name_s, new_name_o, (subject, \
                relation, t_object))

    def _consistency_run_(self, sub, obj, rel_tup):
        if obj not in self.graph:
            self.graph.add_node(obj)
            self.graph.add_edge(sub, obj, relation=set([rel_tup[1]]))
            self.graph.add_edge(obj, sub, relation=set([_bin_rel_(rel_tup[1])]))
            return True
        elif self._check_consistency_(sub, obj, rel_tup):
            self.graph.add_node(obj)
            self.graph.add_edge(sub, obj, relation=set([rel_tup[1]]))
            self.graph.add_edge(obj, sub, relation=set([_bin_rel_(rel_tup[1])]))
            return True
        return False

    def _check_consistency_(self, my_start, my_node, (subject, relation, \
            t_object)):
        G = nx.DiGraph(self.graph)
        if my_node in G:
            if nx.algorithms.shortest_paths.generic.has_path(G, my_start, \
                my_node):
                # print "Z " + str(my_start)
                # print "Do " + str(my_node)
                path = nx.algorithms.shortest_paths.unweighted.predecessor( \
                    G, my_start)
                pred_rel = self._predicted_relation_(path, my_start, my_node)
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
            relation = _comp_rel_(next_rel, relation)
            # print str(next) + " -> " + str(target) + " " + str(relation)
        # print "Happy END"
        return relation

def _bin_rel_(relation):
    if relation == "PP":
        return "PPI"
    return relation

def _lemma_(entity):
    lemmas = psi_toolkit_pipe(entity, "pl")
    return '_'.join([lemmas[iterat].split("|")[0] for iterat in \
        range(len(lemmas)-1)])

if __name__ == '__main__':
    MYSSFB = SimpleSpatialFactsBase("ssfbase.json")
    work_type = sys.argv[1]
    if work_type == "-f":
        for line in sys.stdin:
            parts = line.split("@|@")
            first_name = _lemma_(parts[0])
            second_name = _lemma_(parts[2])
            if len(first_name) != 0 and len(second_name) != 0:
                print "\"" + str((first_name, parts[1], second_name)) + "\" added."
                MYSSFB.inject_facts([(first_name, parts[1], second_name)])
            else:
                print "\"" + line[:-1] + "\" was lemmatized poorly."
        print "Time for the end."
    elif work_type == "-a":
        for line in sys.stdin:
            parts = line.split("@|@")
            first_name = _lemma_(parts[0].decode('unicode-escape'))
            second_name = _lemma_(parts[2].decode('unicode-escape'))
            if len(first_name) > 0 and len(second_name) > 0:
                print "\"" + str((first_name, parts[1], second_name)) + "\" added."
                MYSSFB.check_fact([(first_name, parts[1], second_name)])
            else:
                print "\"" + line[:-1] + "\" was lemmatized poorly."
