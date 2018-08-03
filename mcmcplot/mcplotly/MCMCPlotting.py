#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:54:16 2018

@author: prmiles
"""

# import required packages
from __future__ import division
from .utilities import generate_names, setup_plot_features, make_x_grid
from .utilities import generate_plotly_subplot_coords

import plotly

import warnings

try:
    from statsmodels.nonparametric.kernel_density import KDEMultivariate
except ImportError as e:
    warnings.warn(str("Exception raised importing statsmodels.nonparametric.kernel_density - plot_density_panel will not work. {}".format(e)))

# --------------------------------------------
def plot_density_panel(chains, names = None, hist_on = False, figsizeinches = None):
    '''
    Plot marginal posterior densities

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain for each parameter
        * **names** (:py:class:`list`): List of strings - name of each parameter
        * **hist_on** (:py:class:`bool`): Flag to include histogram on density plot
        * **figsizeinches** (:py:class:`list`): Specify figure size in inches [Width, Height]
    '''
    nsimu, nparam = chains.shape # number of rows, number of columns
    ns1, ns2, names, figsizeinches = setup_plot_features(nparam = nparam, names = names, figsizeinches = figsizeinches)

#    spid = generate_plotly_subplot_coords(nparam = nparam, ns1 = ns1, ns2 = ns2)
#    f = plt.figure(dpi=100, figsize=(figsizeinches)) # initialize figure
#    fig = plotly.tools.make_subplots(rows=ns1, cols=ns2, subplot_titles=(names))
    trace = []
    for ii in range(nparam):
        # define chain
        chain = chains[:,ii].reshape(nsimu,1) # check indexing
        
        # define x grid
        chain_grid = make_x_grid(chain)
        
        # Compute kernel density estimate
        kde = KDEMultivariate(chain, bw = 'normal_reference', var_type = 'c')
        
        trace.append(plotly.graph_objs.Scatter(x = chain_grid, y = kde.pdf(chain_grid)))

    fig = plotly.graph_objs.Figure(data=trace)
    
    plotly.offline.plot(fig, filename = str('{}.html'.format('densly')))

    return fig