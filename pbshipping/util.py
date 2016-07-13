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
# File: util.py
# Description: utility and helper classes and routines supporting the 
#              shipping api client library.
#

import sys
import logging
import json # allow us to override in the future if needed

logger = logging.getLogger("pbshipping")

def utf8(value):
    if isinstance(value, unicode) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    else:
        return value

def encode_dict_utf8(dict_obj):
    for key, value in dict_obj.iteritems():
        key = utf8(key)
        yield (key, utf8(value))