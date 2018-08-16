# PyNAT: Discover external IP addresses and NAT topologies using STUN.
# Copyright (C) 2018 Ariel Antonitis. Licensed under the MIT license.
#
# setup.py
from setuptools import setup

from pynat import __version__, url

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(name='pynat',
      version=__version__,
      description='Discover external IP addresses and NAT topologies using STUN.',
      long_description=long_description,
      author='Ariel Antonitis',
      author_email='arant@mit.edu',
      url=url,
      py_modules=['pynat'],
      package_data={'*': ['README.rst']},
      entry_points={'console_scripts': ['pynat = pynat:main']},
      license='MIT',
      classifiers=['License :: OSI Approved :: MIT License',
                   'Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Topic :: System :: Networking :: Firewalls',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
      python_requires='>=2.7')
