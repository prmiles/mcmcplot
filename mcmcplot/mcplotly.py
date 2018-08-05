#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:54:16 2018

@author: prmiles
"""

# import required packages
from __future__ import division
from .utilities import setup_plot_features, make_x_grid
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

    sprow, spcol = generate_plotly_subplot_coords(nparam = nparam, ns1 = ns1, ns2 = ns2)
#    f = plt.figure(dpi=100, figsize=(figsizeinches)) # initialize figure
    trace_list = []
    for ii in range(nparam):
        # define chain
        chain = chains[:,ii].reshape(nsimu,1) # check indexing
        
        # define x grid
        chain_grid = make_x_grid(chain)
        
        # Compute kernel density estimate
        kde = KDEMultivariate(chain, bw = 'normal_reference', var_type = 'c')
        
        trace_list.append(generate_plotly_trace_object(x = chain_grid.reshape(chain_grid.size), 
                                                       y = kde.pdf(chain_grid).reshape(chain_grid.size,),
                                                       plot_settings = {'label': names[ii]}))
#        trace_list.append(plotly.graph_objs.Scatter(x = chain_grid.reshape(chain_grid.size,), y = kde.pdf(chain_grid).reshape(chain_grid.size,),
#                                                    name = names[ii]))
        
    # make plot
    fig = plotly.tools.make_subplots(rows = ns1, cols = ns2, vertical_spacing = 0.15)
    for ii in range(nparam):
        row = sprow[ii]
        col = spcol[ii]
        print('Generating row = {}, col = {}'.format(row, col))
        fig.append_trace(trace = trace_list[ii], row = row, col = col)
        format_axis(fig, 'y', ii, str('\pi({}|M^{{data}})'.format(names[ii])))
        format_axis(fig, 'x', ii, names[ii])
    
    fig['layout'].update(height=600, width=800, title='densly', showlegend = False)
    plotly.offline.plot(fig, filename = str('{}.html'.format('densly')))

    return fig

def format_axis(fig, axis, ii, title):
    fig['layout'][str('{}axis{}'.format(axis, ii+1))].update(
            title = title,
            linecolor='#636363',
            linewidth=3,
            showgrid=True,
            zeroline=True,
            showline=True,
            mirror='ticks',
            gridcolor='#bdbdbd',
            gridwidth=2,
            position=0.9,)
    
def generate_plotly_trace_object(x, y, plot_settings):
    settings = _plot_settings(plot_settings)      
    trace = plotly.graph_objs.Scatter(
                x = x,
                y = y,
#                hoverinfo = 'label',
                mode='lines',
                line = dict(width = settings['Linewidth'],
                        color = settings['color'],),
                name = settings['label'],
                text = settings['label'],
                )
    return trace

def _plot_settings(user_settings = None, nm = 1):
        if nm == 1:
            dh = 500
            dw = 500
            dmph = 4
            dmpw = 4
        else:
            dh = 1000
            dw = 1000
            dmph = 10
            dmpw = 10
            
        default_settings = {
                'jupyter': False,
                'colorscale': 'Viridis',
                'markersize': 5,
                'filename': 'knot_ml',
                'maintitle': "Knot Machine Learning",
                'height': dh,
                'width': dw,
                'mpheight': dmph,
                'mpwidth': dmpw,
                'color': 'blue',
                'label': None,
                'Linewidth': 3,
                }
        
        settings = default_settings.copy()
        
        options = list(default_settings.keys())
        if user_settings is None:
            user_settings = {}
        user_options = list(user_settings.keys())
        for ii in range(len(user_options)):
            if user_options[ii] in options:
                settings[user_options[ii]] = user_settings[user_options[ii]]
                
        return settings