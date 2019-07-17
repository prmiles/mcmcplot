#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:23:00 2019

@author: prmiles
"""
from mcmcplot import mcmcplot
import unittest


# --------------------------
class MCMCPLOT(unittest.TestCase):

    def test_import(self):
        methods = [
                'plot_density_panel',
                'plot_chain_panel',
                'plot_histogram_panel',
                'plot_pairwise_correlation_panel',
                'plot_chain_metrics',
                'plot_joint_distributions',
                'plot_paired_density_matrix',
                ]
        for method in methods:
            self.assertTrue(hasattr(mcmcplot, method),
                            msg=str('Expect {} assigned'.format(method)))