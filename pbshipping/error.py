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
# File: error.py
# Description: shipping api error classes
#

from pbshipping import util

#
# Error subclass for capturing Shipping API call error 
# - "message" contains the exception error message
# - "http_status" contains the HTTP status code of the call
# - "http_body" contains the original HTTP response body of the call
# - "json_body", if not null, contains a Python dictionary object 
#    representing the JSON response data. 
#
class APIError(Exception):

    def __init__(self, message=None, http_status=None, http_body=None):
        if http_body != None:
            message += " "
            message += http_body
        super(APIError, self).__init__(message)
        
        self.http_status = http_status
        self.http_body = http_body

        self.error_info = []
        json_obj = None
        try:
            json_obj = util.json.loads(http_body)
        except Exception, e:
            json_obj = None
            
        if json_obj != None:
            try:
                # there can be three different formats of error
                if isinstance(json_obj, list):
                    for next_entry in json_obj:
                        error_entry = dict()
                        if "key" in next_entry:
                            error_entry["errorCode"] = next_entry["key"]
                            error_entry["message"] = next_entry["message"]
                        elif "errorCode" in next_entry:
                            error_entry = next_entry
                        else:
                            raise Exception("unexpected error content format")
                        self.error_info.append(error_entry)
                elif "errors" in json_obj:
                    error_list = json_obj["errors"]
                    for next_entry in error_list:
                        error_entry = dict()
                        error_entry["errorCode"] = next_entry["errorCode"]
                        error_entry["message"] = next_entry["errorDescription"]
                        self.error_info.append(error_entry)
                else:
                    raise Exception("unexpected error content format")
            except Exception:
                pass

class AuthenticationError(APIError):
    pass

class MissingResourceAttribute(APIError):
    def __init__(self, missing_attr):
        message = "Attribute %s is missing" % (missing_attr)
        super(MissingResourceAttribute, self).__init__(message)


