#!/usr/bin/env python

# My Awesome Module distutils setup script

import os
from my_module import metadata

# auto-install and download distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

# credit: <http://packages.python.org/an_example_pypi_project/setuptools.html>
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requirements = [
    'argparse',
]

# see here for more options:
# <http://packages.python.org/distribute/setuptools.html>
setup(name=metadata.title,
      version=metadata.version,
      author=metadata.authors[0],
      author_email=metadata.emails[0],
      maintainer=metadata.authors[0],
      maintainer_email=metadata.emails[0],
      url=metadata.url,
      description=metadata.description,
      long_description=read('README.rst'),
      download_url=metadata.url,
      # find a list of classifiers here:
      # <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: ISC License (ISCL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Documentation',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Installation/Setup',
          'Topic :: System :: Software Distribution',
          ],
      packages=find_packages(),
      install_requires=install_requirements,
      zip_safe=False, # don't use eggs
      entry_points={
          'console_scripts': [
              'my_module_runner = my_module.main:main'
          ],
          # if you have a gui, use this
          # 'gui_scripts': [
          #     'my_module_gui = my_module.gui:main'
          # ]
      }
      )
