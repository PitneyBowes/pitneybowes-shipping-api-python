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
# File: requestor.py
# Description: class providing an interface to all shipping resource objects
#              to make REST calls. 
#

import urllib
import urllib2
import urlparse

from pbshipping import util, error, http_client
from pbshipping import Configuration

def construct_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))

class Requestor(object):
    def __init__(self, auth_obj, client=None):
        self.auth_obj = auth_obj
        if client is None:
            self.client = http_client.new_http_client()
        else:
            self.client = client

    def request(self, method, api_group, api_version, api_path, 
                headers, params, post_data):
        method = method.lower()
        
        req_headers = {}
        req_headers.update(self.auth_obj.get_request_header_entry())
        if (method != "get"):
            req_headers["Content-Type"] = "application/json"     
        if headers != None:
            req_headers.update(headers)    
        
        if Configuration.params["is_production"] == False:
            pb_api_server = Configuration.params["sandbox"]
        else:
            pb_api_server = Configuration.params["production"]
        url = pb_api_server + api_group + api_version + api_path

        if params != None and len(params) > 0:
            encoded_params = urllib.urlencode(list(util.encode_dict_utf8(params)))
            url = construct_api_url(url, encoded_params)
        
        try:    
            content, rcode = self.client.request(method, url, post_data, req_headers)
        except urllib2.HTTPError, http_err:
            err_data = http_err.read()
            raise error.APIError(http_err.msg, http_err.getcode(), err_data)               
        except Exception, e:
            raise error.APIError(e)
        
        json_body = None
        if content != None:
            try:
                json_body = util.json.loads(content)
            except Exception, e:
                print "problem decoding json response"
                json_body = None
                 
        if not (200 <= rcode < 300):
            raise error.APIError("", rcode, content)
        
        if json_body is None:
            raise error.APIError("Cannot decode response body from API call: %s "
                                 "(HTTP response code was %d)" % (content, rcode),
                                 rcode, content)
                                                           
        return json_body
