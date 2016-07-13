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
# Description: shipping services authentication logic
#

import base64
import urllib2

from pbshipping import util, error, http_client
from pbshipping import Configuration

#
# TOKEN AUTHENTICATION
# API: POST /oauth/token
#
# Authentication token class
# 
# Authentication and authorization to access the Pitney Bowes Shipping APIs is 
# done by providing an OAUTH token with each request.
#
# Create an instance of the AuthenticationToken class with the desired API
# key and secret. During instance construction, it will perform the initial
# request to acquire an access token. 
# 
# The authorization information (as documented in the Shipping API REST 
# API document) is readily available through the variable "auth_info", 
# while the access token string is available through the variable "access_token"
#
# Note that each access token has a limited life time (the expiration information
# is available through the auth_info variable. 
# Use the method "refresh_token" to re-acquire a token
#
class AuthenticationToken(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = None
        self.auth_info = None
        self.refresh_token()

    def refresh_token(self):
        auth_encoded = base64.b64encode(self.api_key + ':' + self.api_secret)
        req_headers = {"Content-Type" : "application/x-www-form-urlencoded", 
                       "Authorization" : "Basic " + auth_encoded }
        
        post_data = dict()
        post_data['grant_type'] = 'client_credentials'
        
        try:    
            self.access_token = None         
            if Configuration.params["is_production"] == False:
                pb_api_server = Configuration.params["sandbox"]
            else:
                pb_api_server = Configuration.params["production"]      
            client = http_client.new_http_client()         
            content, rcode = client.request("POST", 
                pb_api_server + "/oauth/token", post_data, req_headers)
        except urllib2.HTTPError, http_err:
            err_data = http_err.read()
            raise error.AuthenticationError(http_err.msg, http_err.getcode(), err_data)
        except Exception, e:
            raise error.AuthenticationError(e)
        
        json_body = None
        if content != None:
            try:
                json_body = util.json.loads(content)
            except Exception, e:
                json_body = None

        if not (200 <= rcode < 300):
            raise error.AuthenticationError("", rcode, content)

        if json_body is None:
            raise error.AuthenticationError(
                    "Cannot decode response body properly: %s "
                    "(HTTP response code was %d)" % (content, rcode),
                    rcode, content)   
        
        if "access_token" in json_body:   
            self.access_token = json_body["access_token"]
            self.auth_info = json_body
        else:
            raise error.AuthenticationError("Cannot find access_token in response",
                                            rcode, content)
        
    def get_request_header_entry(self):
        return {"Authorization" : u"Bearer " + self.access_token}
        