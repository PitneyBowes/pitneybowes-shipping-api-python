#
# Copyright 2016 Pitney Bowes Inc.
# Licensed under the MIT License (the "License"); you may not use this file 
# except in compliance with the License.  You may obtain a copy of the License 
# in the LICENSE file or at 
#
#    https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and 
# limitations under the License.
#
# File: setup.py
# Description: Python setup and installation logic for shipping api client 
#              library
#

import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
    from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py
    from distutils.command.build_scripts import build_scripts

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 or earlier is not officially supported. '
        'For any questions, please email us at ShippingAPISupport@pb.com.',
        DeprecationWarning)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pbshipping'))

#from version import VERSION
VERSION = '1.0.4'

setup(name='pbshipping',
      cmdclass={'build_py': build_py, "build_scripts": build_scripts},
      version=VERSION,
      description='Pitney Bowes Shipping API client library for Python',
      url='http://developer.pitneybowes.com/',
      download_url = "https://github.com/PitneyBowes/pitneybowes-shipping-api-python",
      author='Pitney Bowes Shipping API team',
      author_email='ShippingAPISupport@pb.com',
      license='MIT',
      packages=['pbshipping', 'pbshipping.test'],
      test_suite="test",
      #install_requires=install_requires,
      use_2to3=True,
      zip_safe=True,
      keywords=["shipping", 'mailing'],
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ]
      )
