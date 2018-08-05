#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on August 5, 2018

@author: prmiles
"""

import pandas as pd
import seaborn as sns
from .utilities import generate_names, check_settings

def plot_joint_distributions(chains, names = None, sns_style = 'white', settings = None):
    """
    Plot joint distribution for each parameter set.
    
    https://seaborn.pydata.org/generated/seaborn.jointplot.html

    Args:
        * **chains** (:class:`~numpy.ndarray`): Sampling chain for each parameter
        * **names** (:py:class:`list`): List of strings - name of each parameter
        * **figsizeinches** (:py:class:`list`): Specify figure size in inches [Width, Height]
        * **skip** (:py:class:`int`): Indicates step size to be used when plotting elements from the chain
    """
    default_settings = {
        'skip': 1,
        'sns_style': sns_style,
        'sns_settings': sns.axes_style(style = sns_style),
        'jd_settings': dict(kind='kde', stat_func=None, color=None, height=6,
                            ratio=5, space=0, dropna=True, xlim=None, ylim=None,
                            joint_kws=None, marginal_kws=None, annot_kws=None)
        }
    
    settings = check_settings(default_settings = default_settings, user_settings = settings)
    sns.set_style(settings['sns_style'], settings['sns_settings'])
    
    nsimu, nparam = chains.shape # number of rows, number of columns
    
    inds = range(0, nsimu, settings['skip'])
    
    names = generate_names(nparam = nparam, names = names)
      
    g = []
    for jj in range(2,nparam+1):
        for ii in range(1,jj):
            chain1 = pd.Series(chains[inds,ii-1], name=names[ii-1])
            chain2 = pd.Series(chains[inds,jj-1], name=names[jj-1])
            
            # Show the joint distribution using kernel density estimation
            g.append(sns.jointplot(chain1, chain2, **settings['jd_settings']))
            
    return g, settings


    
def plot_paired_density_matrix(chains, names = None, sns_style = 'white', index = None, settings = None):
    default_settings = {
    'skip': 1,
    'sns_style': sns_style,
    'sns_settings': sns.axes_style(style = sns_style),
    'pg_settings': dict(hue=None, hue_order=None, palette=None, hue_kws=None,
                        vars=None, x_vars=None, y_vars=None, diag_sharey=True,
                        height=2.5, aspect=1, despine=True, dropna=True, size=None),
    'ld_type': sns.kdeplot,
    'ld_settings': {},
    'md_type': sns.kdeplot,
    'md_settings': {},
    'ud_type': sns.scatterplot,
    'ud_settings': {},
    }
    settings = check_settings(default_settings = default_settings, user_settings = settings)
    sns.set_style(settings['sns_style'], settings['sns_settings'])
    
    nsimu, nparam = chains.shape # number of rows, number of columns
    names = generate_names(nparam = nparam, names = names)
    
    df = pd.DataFrame(chains, columns = names)
    if index is not None: # a valid categorical column must be appended in order to use hue
        df = df.assign(index = index)
    
    g = sns.PairGrid(df, **settings['pg_settings'])
    g.map_lower(settings['ld_type'], **settings['ld_settings'])
    g.map_upper(settings['ud_type'], **settings['ud_settings'])
    g.map_diag(settings['md_type'], **settings['md_settings'])
    return g, settings