#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 12:21:24 2018

@author: prmiles
"""

from mcmcplot import mcseaborn as MP
from mcmcplot import utilities
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import unittest


# --------------------------
class PlotJointDistributions(unittest.TestCase):

    def test_basic_joint_distributions(self):
        npar = 3
        chains = np.random.random_sample(size=(100, npar))
        f = MP.plot_joint_distributions(chains=chains)
        names = utilities.generate_names(nparam=npar, names=None)
        count = 0
        for jj in range(2, npar+1):
            for ii in range(1, jj):
                name1 = names[ii-1]
                name2 = names[jj-1]
                self.assertEqual(f[count].ax_joint.get_xlabel(), name1,
                                 msg=str('Should be {}'.format(name1)))
                self.assertEqual(f[count].ax_joint.get_ylabel(), name2,
                                 msg=str('Should be {}'.format(name2)))
                count += 1
        plt.close()

    def test_basic_joint_distributions_single_fig(self):
        npar = 2
        chains = np.random.random_sample(size=(100, npar))
        f = MP.plot_joint_distributions(chains=chains)
        names = utilities.generate_names(nparam=npar, names=None)
        for jj in range(2, npar+1):
            for ii in range(1, jj):
                name1 = names[ii-1]
                name2 = names[jj-1]
                self.assertEqual(f.ax_joint.get_xlabel(), name1,
                                 msg=str('Should be {}'.format(name1)))
                self.assertEqual(f.ax_joint.get_ylabel(), name2,
                                 msg=str('Should be {}'.format(name2)))
        plt.close()

    def test_basic_joint_distributions_with_settings(self):
        npar = 3
        chains = np.random.random_sample(size=(100, npar))
        f, settings = MP.plot_joint_distributions(chains=chains,
                                                  return_settings=True)
        names = utilities.generate_names(nparam=npar, names=None)
        count = 0
        for jj in range(2, npar+1):
            for ii in range(1, jj):
                name1 = names[ii-1]
                name2 = names[jj-1]
                self.assertEqual(f[count].ax_joint.get_xlabel(), name1,
                                 msg=str('Should be {}'.format(name1)))
                self.assertEqual(f[count].ax_joint.get_ylabel(), name2,
                                 msg=str('Should be {}'.format(name2)))
                count += 1
        self.assertTrue(isinstance(settings, dict),
                        msg='Expect dictionary output')
        plt.close()


# --------------------------
class PlotPairedGrid(unittest.TestCase):

    def test_basic_paired_grid(self):
        npar = 3
        chains = np.random.random_sample(size=(100, npar))
        f = MP.plot_paired_density_matrix(chains=chains)
        self.assertTrue(isinstance(f, sns.axisgrid.PairGrid),
                        msg='Expect seaborn axisgrid PairGrid object')
        plt.close()
        f, settings = MP.plot_paired_density_matrix(chains=chains,
                                                    return_settings=True)
        self.assertTrue(isinstance(f, sns.axisgrid.PairGrid),
                        msg='Expect seaborn axisgrid PairGrid object')
        self.assertTrue(isinstance(settings, dict),
                        msg='Expect dictionary output')
        plt.close()
