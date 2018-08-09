mcmcplot
========

|docs| |build| |coverage| |license| |codacy| |zenodo|

The `mcmcplot <https://prmiles.wordpress.ncsu.edu/codes/python-packages/mcmcplot/>`_ package is designed to assist in the analysis of sampling chains gathered during a Markov Chain Monte Carlo (MCMC) simulation.  This package was designed with the MCMC code `pymcmcstat <https://prmiles.wordpress.ncsu.edu/codes/python-packages/pymcmcstat/>`_ in mind; however, the plotting routines are amenable to other data sets.  The plotting routines use `matplotlib <https://matplotlib.org/>`_ and `seaborn <https://seaborn.pydata.org/>`_.  User's are recommended to investigate other plotting routines available in `seaborn <https://seaborn.pydata.org/>`_ as it is specifically designed for this sort of analysis.  The routines available in `mcmcplot <https://prmiles.wordpress.ncsu.edu/codes/python-packages/mcmcplot/>`_ serve as a useful wrapper function for several `seaborn <https://seaborn.pydata.org/>`_ plots, but it is not an exhaustive demonstration.

Installation
============

This code can be found on the `Github project page <https://github.com/prmiles/mcmcplot>`_.  The package is available on the PyPI distribution site and the latest version can be installed via
::

    pip install mcmcplot
    
The master branch typically matches the latest version on the PyPI distribution site.  To install the master branch directly from Github,
::

    pip install git+https://github.com/prmiles/mcmcplot.git

You can also clone the repository and run ``python setup.py install``.

Getting Started
===============

- Tutorial `notebooks <https://nbviewer.jupyter.org/github/prmiles/notebooks/tree/master/mcmcplot/index.ipynb>`_
- `Documentation <http://mcmcplot.readthedocs.io/>`_

License
=======

`MIT <https://github.com/prmiles/mcmcplot/blob/master/LICENSE>`_

Contributors
============

See the `GitHub contributor
page <https://github.com/prmiles/mcmcplot/graphs/contributors>`_

Citing mcmcplot
===============

Please see the `mcmcplot homepage <https://prmiles.wordpress.ncsu.edu/codes/python-packages/mcmcplot/>`_ or follow the DOI badge above to find the appropriate citation information.

Feedback
========

- `Feature Request <https://github.com/prmiles/mcmcplot/issues/new?template=feature_request.md>`_
- `Bug Report <https://github.com/prmiles/mcmcplot/issues/new?template=bug_report.md>`_

.. |docs| image:: https://readthedocs.org/projects/mcmcplot/badge/?version=latest
    :target: https://mcmcplot.readthedocs.io/en/latest/?badge=latest
    
.. |build| image:: https://travis-ci.org/prmiles/mcmcplot.svg?branch=master
    :target: https://travis-ci.org/prmiles/mcmcplot
    
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/prmiles/mcmcplot/blob/master/LICENSE.txt
    
.. |codacy| image:: https://api.codacy.com/project/badge/Grade/f806a77eb498459d8d500d9c81e837aa    
    :target: https://www.codacy.com/app/prmiles/mcmcplot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prmiles/mcmcplot&amp;utm_campaign=Badge_Grade
    
.. |coverage| image:: https://coveralls.io/repos/github/prmiles/mcmcplot/badge.svg?branch=master
    :target: https://coveralls.io/github/prmiles/mcmcplot?branch=master
    
.. |zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1341090.svg
    :target: https://doi.org/10.5281/zenodo.1341090
