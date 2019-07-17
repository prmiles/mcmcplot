mcmcplot
========

|docs| |build| |coverage| |license| |zenodo|

The `mcmcplot <https://github.com/prmiles/mcmcplot/wiki>`_ package is designed to assist in the analysis of sampling chains gathered during a Markov Chain Monte Carlo (MCMC) simulation.  This package was designed with the MCMC code `pymcmcstat <https://github.com/prmiles/pymcmcstat/wiki>`_ in mind; however, the plotting routines are amenable to other data sets.  The plotting routines use `matplotlib <https://matplotlib.org/>`_ and `seaborn <https://seaborn.pydata.org/>`_.  User's are recommended to investigate other plotting routines available in `seaborn <https://seaborn.pydata.org/>`_ as it is specifically designed for this sort of analysis.  The routines available in `mcmcplot <https://github.com/prmiles/mcmcplot/wiki>`_ serve as a useful wrapper function for several `seaborn <https://seaborn.pydata.org/>`_ plots, but it is not an exhaustive demonstration.

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

- `Tutorial notebooks <https://github.com/prmiles/mcmcplot_examples>`_
- `Documentation <http://mcmcplot.readthedocs.io/>`_
- `Release history`_

.. _Release history: CHANGELOG.rst

License
=======

`MIT <https://github.com/prmiles/mcmcplot/blob/master/LICENSE>`_

Contributors
============

See the `GitHub contributor
page <https://github.com/prmiles/mcmcplot/graphs/contributors>`_

Citing mcmcplot
===============

Please see the `mcmcplot homepage <https://github.com/prmiles/mcmcplot/wiki>`_ or follow the DOI badge above to find the appropriate citation information.

Feedback
========

- `Feature Request <https://github.com/prmiles/mcmcplot/issues/new?template=feature_request.md>`_
- `Bug Report <https://github.com/prmiles/mcmcplot/issues/new?template=bug_report.md>`_

Sponsor
=======
This work was sponsored in part by the NNSA Office of Defense Nuclear Nonproliferation R&D through the Consortium for Nonproliferation Enabling Capabilities.

|cnec|

.. |docs| image:: https://readthedocs.org/projects/mcmcplot/badge/?version=latest
    :target: https://mcmcplot.readthedocs.io/en/latest/?badge=latest
    
.. |build| image:: https://travis-ci.org/prmiles/mcmcplot.svg?branch=master
    :target: https://travis-ci.org/prmiles/mcmcplot
    
.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/prmiles/mcmcplot/blob/master/LICENSE.txt
    
.. |coverage| image:: https://coveralls.io/repos/github/prmiles/mcmcplot/badge.svg?branch=master
    :target: https://coveralls.io/github/prmiles/mcmcplot?branch=master
    
.. |zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1341090.svg
    :target: https://doi.org/10.5281/zenodo.1341090

.. |cnec| image:: https://raw.githubusercontent.com/prmiles/mcmcplot/master/doc/cnec-logo.png
    :target: https://cnec.ncsu.edu/
