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
# File: authentication.py
# Description: class encapsulating HTTP client call implementation
#

import urllib
import urllib2
from pbshipping import util

# generate a new HTTP client object for API calls
def new_http_client():
    return Urllib2HttpClient()

# base class defining the http client interface
class HttpClient(object):
    def __init__(self):
        pass

    def request(self, method, url, post_data, headers):
        pass

#-------------------------------------------------------------------------------
# pb_urllib2_request_with_method
# - subclass urllib2 class to support all 4 HTTP methods (POST/PUT/GET/DELETE) 
#-------------------------------------------------------------------------------
class pb_urllib2_request_with_method(urllib2.Request):
    def __init__(self, method, *args, **kwargs):
        self._method = method
        urllib2.Request.__init__(self, *args, **kwargs)
        
    def get_method(self):
        return self._method

# urlllib2 based http client
class Urllib2HttpClient(HttpClient):
    def __init__(self):
        pass
    
    def request(self, method, url, post_data, headers):
        if method is "get" or post_data is None:
            post_data_str = ""
        else:
            if post_data is None:
                post_data_str = ""
            else:
                if "Content-Type" not in headers:
                    post_data_str = util.json.dumps(post_data)                    
                elif headers["Content-Type"].lower() == "application/x-www-form-urlencoded":
                    encoded_utf8 = util.encode_dict_utf8(post_data)
                    post_data_str = urllib.urlencode(list(encoded_utf8))             
                else:
                    post_data_str = util.json.dumps(post_data)

        req = pb_urllib2_request_with_method(method, url, post_data_str, headers)
        resp = urllib2.urlopen(req)

        rcode = resp.getcode() 
        content = resp.read()
        
        return content, rcode
