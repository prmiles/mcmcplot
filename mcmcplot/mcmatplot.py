#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:54:16 2018

@author: prmiles
"""

# import required packages
from __future__ import division
import matplotlib.pyplot as plt
from pylab import hist
from .utilities import generate_names, make_x_grid
from .utilities import check_settings, generate_subplot_grid
from .utilities import generate_ellipse_plot_points
from .utilities import setup_subsample
import numpy as np

import warnings

try:
    from statsmodels.nonparametric.kernel_density import KDEMultivariate
except ImportError as e:
    warnings.warn(str("Exception raised importing \
                      statsmodels.nonparametric.kernel_density \
                      - plot_density_panel will not work. {}".format(e)))


# --------------------------------------------
def plot_density_panel(chains, names=None, settings=None,
                       return_kde=False, hist_on=False,
                       return_settings=False):
    '''
    Plot marginal posterior densities

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter. Default: `None`
        * **settings** (:py:class:`dict`): Settings for features \
        of this method. Default: `None`
        * **return_kde** (:py:class:`bool`): Flag to return \
          handles of functions from KDE. Default: `False`
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`
        * **hist_on** (:py:class:`bool`): Flag to include histogram \
          on plot with marginal distribution.

    Returns:
        * If `return_settings=True` and `return_kde=True`, \
          (:py:class:`tuple`): (figure handle, settings used, \
          kde handles)
        * If `return_settings=True` and `return_kde=False`, \
          (:py:class:`tuple`): (figure handle, settings used)
        * If `return_settings=False` and `return_kde=True`, \
          (:py:class:`tuple`): (figure handle, kde handles)
        * Otherwise, figure handle
    '''
    default_settings = {
            'maxpoints': 500,
            'fig': dict(figsize=(5, 4), dpi=100),
            'kde': dict(bw='normal_reference', var_type='c'),
            'plot': dict(color='k', marker=None, linestyle='-', linewidth=3),
            'xlabel': {},
            'ylabel': {},
            'hist': dict(density=True),
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    nsimu, nparam = chains.shape  # number of rows, number of columns
    ns1, ns2 = generate_subplot_grid(nparam)
    names = generate_names(nparam, names)
    kdehandle = []
    f = plt.figure(**settings['fig'])  # initialize figure
    for ii in range(nparam):
        # define chain
        chain = chains[:, ii].reshape(nsimu, 1)  # check indexing
        # define x grid
        chain_grid = make_x_grid(chain)
        # Compute kernel density estimate
        kde = KDEMultivariate(chain, **settings['kde'])
        # plot density on subplot
        plt.subplot(ns1, ns2, ii + 1)
        if hist_on is True:  # include histograms
            hist(chain, **settings['hist'])
        plt.plot(chain_grid, kde.pdf(chain_grid), **settings['plot'])
        # format figure
        plt.xlabel(names[ii], **settings['xlabel'])
        plt.ylabel(str('$\\pi$({}$|M^{}$)'.format(names[ii], '{data}')),
                   **settings['ylabel'])
        plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1.0)  # adjust spacing
        kdehandle.append(kde)
    # setup output
    if return_kde is True and return_settings is True:
        return f, settings, kdehandle
    elif return_kde is True and return_settings is False:
        return f, kdehandle
    elif return_kde is False and return_settings is True:
        return f, settings
    else:
        return f


# --------------------------------------------
def plot_histogram_panel(chains, names=None,
                         settings=None, return_settings=False):
    """
    Plot histogram from each parameter's sampling history

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter. Default: `None`
        * **settings** (:py:class:`dict`): Settings for features \
        of this method. Default: `None`
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    """
    default_settings = {
            'maxpoints': 500,
            'fig': dict(figsize=(5, 4), dpi=100),
            'kde': dict(bw='normal_reference', var_type='c'),
            'hist': dict(density=True),
            'xlabel': {},
            'ylabel': dict(ylabel=''),
            'turn_yticks_on': False,
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    nsimu, nparam = chains.shape  # number of rows, number of columns
    ns1, ns2 = generate_subplot_grid(nparam)
    names = generate_names(nparam, names)
    f = plt.figure(**settings['fig'])  # initialize figure
    for ii in range(nparam):
        # define chain
        chain = chains[:, ii].reshape(nsimu, 1)  # check indexing
        # plot density on subplot
        ax = plt.subplot(ns1, ns2, ii + 1)
        hist(chain, **settings['hist'])
        # format figure
        plt.xlabel(names[ii], **settings['xlabel'])
        plt.ylabel(**settings['ylabel'])
        if settings['turn_yticks_on'] is False:
            ax.get_yaxis().set_ticks([])
        plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1.0)  # adjust spacing
    if return_settings is True:
        return f, settings
    else:
        return f


# --------------------------------------------
def plot_chain_panel(chains, names=None, settings=None,
                     skip=1, maxpoints=500, return_settings=False):
    """
    Plot sampling chain for each parameter

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
        of each parameter
        * **settings** (:py:class:`dict`): Settings for features \
        of this method.
        * **skip** (:py:class:`int`): Indicates step size to be used when
          plotting elements from the chain
        * **maxpoints** (:py:class:`int`): Max number of display points
          - keeps scatter plot from becoming overcrowded
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    """
    default_settings = {
            'fig': dict(figsize=(5, 4), dpi=100),
            'plot': dict(color='b', marker='.', linestyle='none'),
            'xlabel': {'xlabel': 'Iteration'},
            'ylabel': {},
            'add_pm2std': False,
            'mean': dict(color='k', marker=None, linestyle='-', linewidth=3),
            'sig': dict(color='r', marker=None, linestyle='--', linewidth=3),
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)

    nsimu, nparam = chains.shape  # number of rows, number of columns
    ns1, ns2 = generate_subplot_grid(nparam)
    names = generate_names(nparam, names)
    # setup sample indices
    inds = setup_subsample(skip, maxpoints, nsimu)
    f = plt.figure(**settings['fig'])  # initialize figure
    for ii in range(nparam):
        # define chain
        chain = chains[inds, ii]  # check indexing
        # plot chain on subplot
        plt.subplot(ns1, ns2, ii + 1)
        plt.plot(inds, chain,
                 **settings['plot'])
        # format figure
        plt.xlabel(**settings['xlabel'])
        plt.ylabel(str('{}'.format(names[ii])), **settings['ylabel'])
        if ii + 1 <= ns1*ns2 - ns2:
            plt.xlabel('')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1.0)  # adjust spacing
        if settings['add_pm2std'] is True:
            mu = np.mean(chain)
            sig = np.std(chain)
            plt.plot(inds, np.ones(inds.shape)*mu,
                     **settings['mean'])
            plt.plot(inds, np.ones(inds.shape)*mu + 2*sig,
                     **settings['sig'])
            plt.plot(inds, np.ones(inds.shape)*mu - 2*sig,
                     **settings['sig'])
    if return_settings is True:
        return f, settings
    else:
        return f


# --------------------------------------------
def plot_pairwise_correlation_panel(chains, names=None, settings=None,
                                    skip=1, maxpoints=500,
                                    return_settings=False):
    """
    Plot pairwise correlation for each parameter

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
          for each parameter

    Kwargs:
        * **names** (:py:class:`list`): List of strings - name \
          of each parameter
        * **settings** (:py:class:`dict`): Settings for figure \
          features made by this method.
        * **skip** (:py:class:`int`): Indicates step size to be used when
          plotting elements from the chain
        * **maxpoints** (py:class:`int`): Maximum allowable number of points
          in plot.
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    """
    default_settings = {
            'fig': dict(figsize=(7, 5), dpi=100),
            'plot': dict(color='b', marker='.', linestyle='none'),
            'xlabel': {},
            'ylabel': {},
            'title': {},
            'add_5095_contours': False,
            'plot_50': dict(color='g', marker=None,
                            linewidth=2, linestyle='--', label='50%'),
            'plot_95': dict(color='r', marker=None,
                            linewidth=2, linestyle='--', label='95%'),
            'add_legend': False,
            'legend': dict(loc=1),
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    nsimu, nparam = chains.shape  # number of rows, number of columns
    ns1, ns2 = generate_subplot_grid(nparam)
    names = generate_names(nparam, names)
    inds = setup_subsample(skip, maxpoints, nsimu)
    f = plt.figure(**settings['fig'])  # initialize figure
    for jj in range(2, nparam + 1):
        for ii in range(1, jj):
            chain1 = chains[inds, ii - 1]
            # chain1 = chain1.reshape(nsimu, 1)
            chain2 = chains[inds, jj - 1]
            # chain2 = chain2.reshape(nsimu, 1)
            # plot density on subplot
            ax = plt.subplot(nparam - 1, nparam - 1, (jj - 2)*(nparam - 1)+ii)
            plt.plot(chain1, chain2, **settings['plot'])
            # format figure
            if jj != nparam:  # rm xticks
                ax.set_xticklabels([])
            if ii != 1:  # rm yticks
                ax.set_yticklabels([])
            if ii == 1:  # add ylabels
                plt.ylabel(str('{}'.format(names[jj - 1])),
                           **settings['ylabel'])
            if ii == jj - 1:
                if nparam == 2:  # add xlabels
                    plt.xlabel(str('{}'.format(names[ii - 1])),
                               **settings['xlabel'])
                else:  # add title
                    plt.title(str('{}'.format(names[ii - 1])),
                              **settings['title'])
            if settings['add_5095_contours'] is True:
                contours = generate_ellipse_plot_points(
                        x=chain1, y=chain2, ndp=100)
                plt.plot(contours['xe50'], contours['ye50'],
                         **settings['plot_50'])
                plt.plot(contours['xe95'], contours['ye95'],
                         **settings['plot_95'])
    # adjust figure margins
    plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1.0)  # adjust spacing
    if settings['add_legend'] is True:
        ax = plt.gca()
        h, labs = ax.get_legend_handles_labels()
        plt.figlegend(h, labs, **settings['legend'])
    if return_settings is True:
        return f, settings
    else:
        return f


# --------------------------------------------
def plot_chain_metrics(chain, name=None, settings=None,
                       return_settings=False):
    '''
    Plot chain metrics for individual chain

    - Scatter plot of chain
    - Histogram of chain

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain \
        for specific parameter

    Kwargs:
        * **names** (:py:class:`str`): Name of each parameter
        * **settings** (:py:class:`dict`): Settings for features \
        of this method.
        * **return_settings** (:py:class:`bool`): Flag to return \
        figure settings. Default: `False`

    Returns:
        * If `return_settings=True`, (:py:class:`tuple`): \
        (figure handle, settings actually used in program)
        * Otherwise, figure handle
    '''
    default_settings = {
            'skip': 1,
            'fig': dict(figsize=(7, 5), dpi=100),
            'suptitle': dict(fontsize=12),
            'plot': dict(color='b', marker='.', linestyle='none'),
            'hist': dict(density=True),
            'xlabel': {},
            'ylabel': {},
            }
    settings = check_settings(
            default_settings=default_settings, user_settings=settings)
    name = generate_names(nparam=1, names=name)[0]
    f = plt.figure(**settings['fig'])  # initialize figure
    plt.suptitle('Chain metrics for {}'.format(name), **settings['suptitle'])
    plt.subplot(2, 1, 1)
    plt.plot(range(0, len(chain)), chain, **settings['plot'])
    # format figure
    plt.xlabel('Iterations', **settings['xlabel'])
    plt.ylabel(str('{}-chain'.format(name)), **settings['ylabel'])
    # Add histogram
    plt.subplot(2, 1, 2)
    hist(chain, **settings['hist'])
    # format figure
    plt.xlabel(name, **settings['xlabel'])
    plt.ylabel(str('Histogram of {}-chain'.format(name)), **settings['ylabel'])
    plt.tight_layout(rect=[0, 0.03, 1, 0.95], h_pad=1.0)  # adjust spacing
    if return_settings is True:
        return f, settings
    else:
        return f
