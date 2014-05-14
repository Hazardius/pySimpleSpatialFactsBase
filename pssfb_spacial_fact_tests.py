#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pssfb_spacial_fact import rel_type, spacial_fact

class pssfb_spacial_fact_tests(unittest.TestCase):

    def test_sf_representation(self):
        results = str(spacial_fact("Polska", rel_type.PP, "Europa"))
        expected = "Polska set(['PP']) Europa"
        self.assertEqual(expected, results)

    def test_sf_get_id(self):
        results = str(spacial_fact("Polska", rel_type.PP, "Europa").get_id())
        expected = "Polska --PP-> Europa"
        self.assertEqual(expected, results)

    def test_sf_simple_compose_1(self):
        fact1 = spacial_fact("Polska", rel_type.PP, "Europa")
        fact2 = spacial_fact("Europa", rel_type.PPI, "Austria")
        results = str(fact1.compose(fact2))
        # TODO: To make independent of the order.
        expected = "Polska set(['EQ', 'PP', 'DR', 'PO', 'PPI']) Austria"
        self.assertEqual(expected,results)

    def test_sf_simple_compose_2(self):
        fact1 = spacial_fact("Polska", rel_type.PO, "Odra")
        fact2 = spacial_fact("Odra", rel_type.PP, "Europa")
        results = str(fact1.compose(fact2))
        # TODO: To make independent of the order.
        expected = "Polska set(['PP', 'PO']) Europa"
        self.assertEqual(expected,results)

    def test_sf_simple_compose_3(self):
        fact1 = spacial_fact("Polska", rel_type.PP, "Europa")
        fact2 = spacial_fact("Europa", rel_type.DR, "Ameryka")
        results = str(fact1.compose(fact2))
        expected = "Polska set(['DR']) Ameryka"
        self.assertEqual(expected,results)

if __name__ == '__main__':
    unittest.main()
