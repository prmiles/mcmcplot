#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:35:08 2018

@author: prmiles
"""
import numpy as np
import os


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


# define test model function
def modelfun(xdata, theta):
    m = theta[0]
    b = theta[1]
    nrow = xdata.shape[0]
    y = np.zeros([nrow, 1])
    y[:, 0] = m*xdata.reshape(nrow,) + b
    return y


def ssfun(theta, data, local=None):
    xdata = data.xdata[0]
    ydata = data.ydata[0]
    # eval model
    ymodel = modelfun(xdata, theta)
    # calc sos
    ss = sum((ymodel[:, 0] - ydata[:, 0])**2)
    return ss


# define test model function
def predmodelfun(data, theta):
    m = theta[0]
    b = theta[1]
    nrow = data.xdata[0].shape[0]
    y = np.zeros([nrow, 1])
    y[:, 0] = m*data.xdata[0].reshape(nrow,) + b
    return y


def setup_pseudo_results():
    results = {
            'chain': np.random.random_sample(size=(100, 2)),
            's2chain': np.random.random_sample(size=(100, 1)),
            'sschain': np.random.random_sample(size=(100, 1)),
            'parind': np.array([[0, 1]]),
            'local': np.array([[0, 0]]),
            'model_settings': {'nbatch': np.random.random_sample(
                    size=(100, 1))},
            'theta': np.random.random_sample(size=(2, )),
            'sstype': np.random.random_sample(size=(1, 1)),
            }
    return results


def setup_pseudo_ci():
    ci = []
    ci1 = []
    ci1.append([np.random.random_sample(size=(100,)),
                np.random.random_sample(size=(100,)),
                np.random.random_sample(size=(100,))])
    ci.append(ci1)
    return ci


def generate_temp_folder():
    tmpfolder = 'temp0'
    count = 0
    flag = True
    while flag is True:
        if os.path.isdir(str('{}'.format(tmpfolder))):
            count += 1
            tmpfolder = str('{}{}'.format('temp', count))
        else:
            flag = False
    return tmpfolder


def generate_temp_file(extension='h5'):
    tmpfile = str('temp0.{}'.format(extension))
    count = 0
    flag = True
    while flag is True:
        if os.path.isfile(str('{}'.format(tmpfile))):
            count += 1
            tmpfile = str('{}{}.{}'.format('temp', count, extension))
        else:
            flag = False
    return tmpfile
