#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on August 5, 2018

@author: prmiles
"""

import pandas as pd
import seaborn as sns
from .utilities import generate_names, check_settings


def plot_joint_distributions(chains, names=None, sns_style='white',
                             settings=None):
    """
    Plot joint distribution for each parameter set.

    https://seaborn.pydata.org/generated/seaborn.jointplot.html

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter
        * **sns_style** (:py:class:`str`): Style for seaborn plot. \
        Default is `white`.
        * **settings** (:py:class:`dict`): Settings for features \
        of this method.

    Returns:
        * (:py:class:`tuple`): (figure handle, settings actually \
        used in program)
    """
    default_settings = {
            'skip': 1,
            'sns_style': sns_style,
            'sns': sns.axes_style(style=sns_style),
            'jointplot': dict(kind='kde', data=None, height=6.0, space=0)
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    sns.set_style(settings['sns_style'], settings['sns'])
    nsimu, nparam = chains.shape  # number of rows, number of columns
    names = generate_names(nparam=nparam, names=names)
    inds = range(0, nsimu, settings['skip'])
    g = []
    for jj in range(2, nparam+1):
        for ii in range(1, jj):
            chain1 = pd.Series(chains[inds, ii-1], name=names[ii-1])
            chain2 = pd.Series(chains[inds, jj-1], name=names[jj-1])
            # Show the joint distribution using kernel density estimation
            a = sns.jointplot(x=chain1, y=chain2, **settings['jointplot'])
            g.append(a)
    return g, settings


def plot_paired_density_matrix(chains, names=None, sns_style='white',
                               index=None, settings=None):
    """
    Plot paired density matrix.

    https://seaborn.pydata.org/generated/seaborn.PairGrid.html

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter
        * **sns_style** (:py:class:`str`): Style for seaborn plot. \
        Default is `white`.
        * **settings** (:py:class:`dict`): Settings for features \
        of this method.

    Returns:
        * (:py:class:`tuple`): (figure handle, settings actually \
        used in program)
    """
    default_settings = {
            'skip': 1,
            'sns_style': sns_style,
            'sns': sns.axes_style(style=sns_style),
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
    sns.set_style(settings['sns_style'], settings['sns'])
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
    return g, settings


class Plot:
    '''
    Wrapper routines for analyzing/plotting sampling chains from MCMC process.

    Uses methods from the `seaborn` package:

    https://seaborn.pydata.org/

    Attributes:
        - :meth:`~plot_joint_distributions`
        - :meth:`~plot_paired_density_matrix`
    '''
    def __init__(self):
        self.plot_joint_distributions = plot_joint_distributions
        self.plot_paired_density_matrix = plot_paired_density_matrix
