"""Setup file for the Cleo package.

   Adapted from the Python Packaging Authority template."""

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import importlib

# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def check_dependencies(package_names):
    """Check if packages can be imported, if not throw a message."""
    not_met = []
    for n in package_names:
        try:
            _ = importlib.import_module(n)
        except ImportError:
            not_met.append(n)
    if len(not_met) != 0:
        raise ImportError("Following packages could not be found: " + ', '.join(not_met))

req_packages = ['salem']

check_dependencies(req_packages)


setup(
    # Project info
    name='Cleo',
    version='0.0.1',
    description='Plotting on map projections.',
    long_description=long_description,
    # The project's main homepage.
    url='https://github.com/fmaussion/cleo',
    # Author details
    author='Fabien Maussion',
    author_email='fabien.maussion@uibk.ac.at',
    # License
    license='GPLv3+',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha  4 - Beta  5 - Production/Stable
        'Development Status :: 4 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: GNU General Public License '
        'v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    # What does your project relate to?
    keywords=['gis', 'climate', 'graphics'],
    # Find packages automatically
    packages=find_packages(exclude=['docs']),
    # Decided not to let pip install the dependencies, this is too brutal
    install_requires=[],
    # List additional groups of dependencies here (e.g. development dependencies).
    extras_require={},
    # data files that need to be installed
    package_data={'cleo.files': ['*'],
                  'cleo.tests.baseline_images': ['*']
                  },
    # Old
    data_files=[],
    # Executable scripts
    entry_points={},
)
