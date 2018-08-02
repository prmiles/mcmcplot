from setuptools import setup
import codecs

def read(fname):
    with codecs.open(fname, 'r', 'latin') as f:
        return f.read()
    
# read in version number
version_dummy = {}
exec(read('mcmcplotly/__version__.py'), version_dummy)
__version__ = version_dummy['__version__']
del version_dummy

setup(
    name='mcmcplotly',
    version=__version__,
    description='A library to plot and analyze chains from mcmc simulations using plotly',
    url='https://github.com/prmiles/mcmcplot',
    download_url='https://github.com/prmiles/mcmcplotly',
    author='Paul Miles',
    author_email='prmiles@ncsu.edu',
    license='MIT',
    package_dir={'mcmcplotly': 'mcmcplotly'},
    packages=['mcmcplotly'],
    zip_safe=False,
    install_requires=['numpy>=1.7', 'scipy>=0.16', 'plotly'],
    extras_require = {'docs':['sphinx'], 'plotting':['matplotlib', 'plotly'],},
    classifiers=['License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6',
                   'Framework :: IPython',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering',
                   ]
)
