#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 05:57:34 2018

@author: prmiles
"""

from mcmcplot import utilities
import unittest
from mock import patch
import numpy as np
import math


# --------------------------
class CheckSettings(unittest.TestCase):
    def test_settings_with_subdict(self):
        user_settings = dict(a=True, fontsize=12)
        default_settings = dict(a=False, linewidth=3,
                                marker=dict(markersize=5, color='g'))
        settings = utilities.check_settings(
                default_settings=default_settings,
                user_settings=user_settings)
        self.assertEqual(settings['a'],
                         user_settings['a'],
                         msg='Expect user setting to overwrite')
        self.assertEqual(settings['marker'],
                         default_settings['marker'],
                         msg='Expect default to persist')

    def test_settings_with_subdict_user_ow(self):
        user_settings = dict(a=True, fontsize=12,
                             marker=dict(color='b'))
        default_settings = dict(a=False, linewidth=3,
                                marker=dict(markersize=5, color='g'))
        settings = utilities.check_settings(
                default_settings=default_settings,
                user_settings=user_settings)
        self.assertEqual(settings['a'],
                         user_settings['a'],
                         msg='Expect user setting to overwrite')
        self.assertEqual(settings['marker']['color'],
                         user_settings['marker']['color'],
                         msg='Expect user to overwrite')
        self.assertEqual(settings['marker']['markersize'],
                         default_settings['marker']['markersize'],
                         msg='Expect default to persist')

    def test_settings_with_subdict_user_has_new_setting(self):
        user_settings = dict(a=True, fontsize=12,
                             marker=dict(color='b'), linestyle='--')
        default_settings = dict(a=False, linewidth=3,
                                marker=dict(markersize=5, color='g'))
        settings = utilities.check_settings(
                default_settings=default_settings,
                user_settings=user_settings)
        self.assertEqual(settings['a'],
                         user_settings['a'],
                         msg='Expect user setting to overwrite')
        self.assertEqual(settings['marker']['color'],
                         user_settings['marker']['color'],
                         msg='Expect user to overwrite')
        self.assertEqual(settings['marker']['markersize'],
                         default_settings['marker']['markersize'],
                         msg='Expect default to persist')
        self.assertEqual(settings['linestyle'], user_settings['linestyle'],
                         msg='Expect user setting to be added')


# --------------------------
class GenerateSubplotGrid(unittest.TestCase):
    def test_generate_subplot_grid(self):
        nparam = 5
        ns1, ns2 = utilities.generate_subplot_grid(nparam=nparam)
        self.assertEqual(ns1, math.ceil(math.sqrt(nparam)), msg='Expect 3')
        self.assertEqual(ns2, round(math.sqrt(nparam)), msg='Expect 2')

    def test_generate_subplot_grid_1(self):
        nparam = 1
        ns1, ns2 = utilities.generate_subplot_grid(nparam=nparam)
        self.assertEqual(ns1, math.ceil(math.sqrt(nparam)), msg='Expect 1')
        self.assertEqual(ns2, round(math.sqrt(nparam)), msg='Expect 1')


# --------------------------
class GenerateNames(unittest.TestCase):

    def test_default_names(self):
        nparam = 8
        names = utilities.generate_names(nparam=nparam, names=None)
        self.assertEqual(len(names), nparam,
                         msg='Length of names should match number \
                         of parameters')
        for ii in range(nparam):
            self.assertEqual(names[ii], str('$p_{{{}}}$'.format(ii)))

    def test_names_partial(self):
        nparam = 8
        names = ['hi']
        names = utilities.generate_names(nparam=nparam, names=names)
        self.assertEqual(names[0], 'hi', msg='First name is hi')
        for ii in range(1, nparam):
            self.assertEqual(names[ii], str('$p_{{{}}}$'.format(ii)))


# --------------------------
class GenerateDefaultNames(unittest.TestCase):

    def test_size_of_default_names(self):
        nparam = 8
        names = utilities.generate_default_names(nparam=nparam)
        self.assertEqual(len(names), nparam,
                         msg='Length of names should match number \
                         of parameters')

    def test_value_of_default_names(self):
        names = utilities.generate_default_names(nparam=3)
        expected_names = ['$p_{0}$', '$p_{1}$', '$p_{2}$']
        self.assertEqual(names, expected_names,
                         msg=str('Names do not match: Expected - {}, \
                                 Received - {}'.format(expected_names, names)))


# --------------------------
class ExtendNamesToMatchNparam(unittest.TestCase):

    def test_initially_empty_name_set(self):
        nparam = 3
        names = utilities.extend_names_to_match_nparam(
                names=None, nparam=nparam)
        expected_names = ['$p_{0}$', '$p_{1}$', '$p_{2}$']
        self.assertEqual(names, expected_names,
                         msg=str('Names do not match: Expected - {}, \
                                 Received - {}'.format(expected_names, names)))

    def test_single_entry_name_set(self):
        nparam = 3
        names = ['aa']
        names = utilities.extend_names_to_match_nparam(
                names=names, nparam=nparam)
        expected_names = ['aa', '$p_{1}$', '$p_{2}$']
        self.assertEqual(names, expected_names,
                         msg=str('Names do not match: Expected - {}, \
                                 Received - {}'.format(expected_names, names)))

    def test_double_entry_name_set(self):
        nparam = 3
        names = ['aa', 'zz']
        names = utilities.extend_names_to_match_nparam(
                names=names, nparam=nparam)
        expected_names = ['aa', 'zz', '$p_{2}$']
        self.assertEqual(names, expected_names,
                         msg=str('Names do not match: Expected - {}, \
                                 Received - {}'.format(expected_names, names)))


# --------------------------
class MakeXGrid(unittest.TestCase):

    def test_shape_of_output(self):
        x = np.linspace(0, 10, num=50)
        npts = 20
        xgrid = utilities.make_x_grid(x=x, npts=20)
        self.assertEqual(xgrid.shape, (npts, 1),
                         msg=str('Expected return dimension of ({}, 1)'
                                 .format(npts)))

    def test_default_shape_of_output(self):
        x = np.linspace(0, 10, num=50)
        xgrid = utilities.make_x_grid(x=x)
        self.assertEqual(xgrid.shape, (100, 1),
                         msg='Expected return dimension of (100, 1)')

    def test_shape_of_output_for_dense_x(self):
        x = np.linspace(0, 10, num=500)
        npts = 20
        xgrid = utilities.make_x_grid(x=x, npts=20)
        self.assertEqual(xgrid.shape, (npts, 1),
                         msg='Expected return dimension of (npts, 1)')

    def test_default_shape_of_output_for_dense_x(self):
        x = np.linspace(0, 10, num=500)
        xgrid = utilities.make_x_grid(x=x)
        self.assertEqual(xgrid.shape, (100, 1),
                         msg='Expected return dimension of (100, 1)')


# --------------------------
class GenerateEllipse(unittest.TestCase):

    def test_does_non_square_matrix_return_error(self):
        cmat = np.zeros([3, 2])
        mu = np.zeros([2, 1])
        with self.assertRaises(SystemExit):
            utilities.generate_ellipse(mu, cmat)

    def test_does_non_symmetric_matrix_return_error(self):
        cmat = np.array([[3, 2], [1, 3]])
        mu = np.zeros([2, 1])
        with self.assertRaises(SystemExit):
            utilities.generate_ellipse(mu, cmat)

    def test_does_non_positive_definite_matrix_return_error(self):
        cmat = np.zeros([2, 2])
        mu = np.zeros([2, 1])
        with self.assertRaises(SystemExit):
            utilities.generate_ellipse(mu, cmat)

    def test_does_good_matrix_return_equal_sized_xy_arrays(self):
        cmat = np.eye(2)
        mu = np.zeros([2, 1])
        x, y = utilities.generate_ellipse(mu, cmat)
        self.assertEqual(x.shape, y.shape)

    def test_does_good_matrix_return_correct_size_array(self):
        cmat = np.eye(2)
        mu = np.zeros([2, 1])
        ndp = 50  # number of points to generate ellipse shape
        x, y = utilities.generate_ellipse(mu, cmat, ndp)
        self.assertEqual(x.size, ndp)
        self.assertEqual(y.size, ndp)


# --------------------------
class GaussianDensityFunction(unittest.TestCase):

    def test_float_return_with_float_input(self):
        self.assertTrue(
                isinstance(utilities.gaussian_density_function(x=0.),
                           float), msg='Expected float return')

    def test_float_return_with_int_input(self):
        self.assertTrue(
                isinstance(utilities.gaussian_density_function(x=0),
                           float), msg='Expected float return')

    def test_float_return_with_float_input_at_nondefault_mean(self):
        self.assertTrue(
                isinstance(utilities.gaussian_density_function(x=0., mu=100),
                           float), msg='Expected float return')


# --------------------------
class IQrange(unittest.TestCase):

    def test_array_return_with_column_vector_input(self):
        x = np.random.random_sample(size=(100, 1))
        q = utilities.iqrange(x=x)
        self.assertTrue(isinstance(q, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(q)))
        self.assertEqual(q.size, 1, msg='Expect single element array')

    def test_array_return_with_row_vector_input(self):
        x = np.random.random_sample(size=(1, 100))
        q = utilities.iqrange(x=x)
        self.assertTrue(isinstance(q, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(q)))
        self.assertEqual(q.size, 1, msg='Expect single element array')


# --------------------------
class ScaleBandWidth(unittest.TestCase):

    def test_array_return_with_column_vector_input(self):
        x = np.random.random_sample(size=(100, 1))
        s = utilities.scale_bandwidth(x=x)
        self.assertTrue(isinstance(s, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(s)))
        self.assertEqual(s.size, 1, msg='Expect single element array')

    def test_array_return_with_row_vector_input(self):
        x = np.random.random_sample(size=(1, 100))
        s = utilities.scale_bandwidth(x=x)
        self.assertTrue(isinstance(s, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(s)))
        self.assertEqual(s.size, 1, msg='Expect single element array')

    @patch('mcmcplot.utilities.iqrange', return_value=-1.0)
    def test_array_return_with_iqrange_lt_0(self, mock_iqrange):
        x = np.random.random_sample(size=(1, 100))
        s = utilities.scale_bandwidth(x=x)
        self.assertTrue(isinstance(s, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(s)))
        self.assertEqual(s.size, 1, msg='Expect single element array')

    @patch('mcmcplot.utilities.iqrange', return_value=1.0)
    def test_array_return_with_iqrange_gt_0(self, mock_iqrange):
        x = np.random.random_sample(size=(1, 100))
        s = utilities.scale_bandwidth(x=x)
        self.assertTrue(isinstance(s, np.ndarray),
                        msg='Expected array return \
                        - received {}'.format(type(s)))
        self.assertEqual(s.size, 1, msg='Expect single element array')


# --------------------------
class AppendToNrowNcolBasedOnShape(unittest.TestCase):
    def test_shape_is_2d(self):
        nrow = []
        ncol = []
        sh = (2, 1)
        nrow, ncol = utilities.append_to_nrow_ncol_based_on_shape(
                sh=sh, nrow=nrow, ncol=ncol)
        self.assertEqual(nrow, [2], msg='Expect [2]')
        self.assertEqual(ncol, [1], msg='Expect [1]')

    def test_shape_is_1d(self):
        nrow = []
        ncol = []
        sh = (2,)
        nrow, ncol = utilities.append_to_nrow_ncol_based_on_shape(
                sh=sh, nrow=nrow, ncol=ncol)
        self.assertEqual(nrow, [2], msg='Expect [2]')
        self.assertEqual(ncol, [1], msg='Expect [1]')


# --------------------------
class SetupSubsample(unittest.TestCase):

    def test_max_lt_nsimu(self):
        skip = 1
        maxpoints = 10
        nsimu = 100
        inds = utilities.setup_subsample(skip, maxpoints, nsimu)
        self.assertTrue(isinstance(inds, np.ndarray),
                        msg='Expect numpy array')
        self.assertEqual(inds.shape, (10,), msg='Expect (10,)')

    def test_max_gt_nsimu(self):
        skip = 1
        maxpoints = 1000
        nsimu = 100
        inds = utilities.setup_subsample(skip, maxpoints, nsimu)
        self.assertTrue(isinstance(inds, np.ndarray),
                        msg='Expect numpy array')
        self.assertEqual(inds.shape, (100,), msg='Expect (100,)')
        skip = 3
        maxpoints = 1000
        nsimu = 100
        inds = utilities.setup_subsample(skip, maxpoints, nsimu)
        self.assertTrue(isinstance(inds, np.ndarray),
                        msg='Expect numpy array')
        self.assertEqual(inds.shape, (34,), msg='Expect (34,)')

    def test_max_eq_nsimu(self):
        skip = 1
        maxpoints = 100
        nsimu = 100
        inds = utilities.setup_subsample(skip, maxpoints, nsimu)
        self.assertTrue(isinstance(inds, np.ndarray),
                        msg='Expect numpy array')
        self.assertEqual(inds.shape, (100,), msg='Expect (100,)')
