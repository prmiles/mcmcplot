# -*- coding: utf-8 -*-

import unittest
import mcmcplot


class ImportMCMCPlot(unittest.TestCase):

    def test_version_attribute(self):
        version = mcmcplot.__version__
        self.assertTrue(isinstance(version, str),
                        msg='Expect string output')
        self.assertEqual(len(version.split('.')), 3,
                         msg='Expect #.#.# format')
