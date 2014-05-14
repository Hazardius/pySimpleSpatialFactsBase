#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from __init__ import SimpleSpatialFactsBase

class pssfb_tests(unittest.TestCase):

    def test_comp_number(self):
        results = SimpleSpatialFactsBase("other.db").get_comp_nr()
        expected = 0
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
