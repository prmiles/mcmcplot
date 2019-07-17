#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on August 5, 2018

@author: prmiles
"""

import pandas as pd
import seaborn as sns
from .utilities import generate_names, check_settings
from .utilities import setup_subsample


def plot_joint_distributions(chains, names=None,
                             settings=None, maxpoints=500, skip=1,
                             return_settings=False):
    """
    Plot joint distribution for each parameter set.

    https://seaborn.pydata.org/generated/seaborn.jointplot.html

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter. Default: `None`
        * **settings** (:py:class:`dict`): Settings for features \
        of this method. Default: `None`
        * **skip** (:py:class:`int`): Indicates step size to be used when
          sampling elements from the chain. Default: `1`
        * **maxpoints** (:py:class:`int`): Max number of sample points
          - keeps generation of KDE shorter. Default: `500`
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    """
    default_settings = dict(
            kind='kde',
            data=None,
            height=6.0,
            space=0)
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    nsimu, nparam = chains.shape  # number of rows, number of columns
    names = generate_names(nparam=nparam, names=names)
    # setup sample indices
    inds = setup_subsample(skip, maxpoints, nsimu)
    g = []
    for jj in range(2, nparam + 1):
        for ii in range(1, jj):
            chain1 = pd.Series(chains[inds, ii - 1],
                               name=names[ii - 1])
            chain2 = pd.Series(chains[inds, jj - 1],
                               name=names[jj - 1])
            # Show the joint distribution using kernel density estimation
            a = sns.jointplot(x=chain1, y=chain2, **settings)
            g.append(a)
    if len(g) == 1:
        g = g[0]  # return handle instead of list
    if return_settings is True:
        return g, settings
    else:
        return g


def plot_paired_density_matrix(chains, names=None,
                               index=None, settings=None,
                               return_settings=False):
    """
    Plot paired density matrix.

    https://seaborn.pydata.org/generated/seaborn.PairGrid.html

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter. Default: `None`
        * **settings** (:py:class:`dict`): Settings for features \
        of this method. Default: `None`
        * **index** (:py:class:`list`): Category for each row of \
        chain. Default: `None`
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    """
    default_settings = {
            'skip': 1,
            'pairgrid': dict(diag_sharey=False, height=2.5),
            'ld_type': sns.kdeplot,
            'ld': {},
            'md_type': sns.kdeplot,
            'md': {},
            'ud_type': sns.scatterplot,
            'ud': {},
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    nsimu, nparam = chains.shape  # number of rows, number of columns
    names = generate_names(nparam=nparam, names=names)
    df = pd.DataFrame(chains, columns=names)
    # A valid categorical column must be appended in order to use hue
    if index is not None:
        df = df.assign(index=index)
    g = sns.PairGrid(df, **settings['pairgrid'])
    g.map_lower(settings['ld_type'], **settings['ld'])
    g.map_upper(settings['ud_type'], **settings['ud'])
    g.map_diag(settings['md_type'], **settings['md'])
    if return_settings is True:
        return g, settings
    else:
        return g
