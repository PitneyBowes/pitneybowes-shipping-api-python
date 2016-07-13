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
# File: resource.py
# Description: foundation classes for representing an API resoource
#

from pbshipping import requestor

def convert_to_APIObject(v):
    if isinstance(v, list):
        return [convert_to_APIObject(i) for i in v]
    elif isinstance(v, dict) and not isinstance(v, APIObject):
        return APIObject(v)
    else:
        return v
        
class APIObject(dict):
    
    def __init__(self, *args, **kwargs):
        super(APIObject, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = convert_to_APIObject(v)
        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = convert_to_APIObject(v)
    
    def __getattr__(self, attr):
        return self.get(attr)
        
    def __setattr__(self, key, value):
        self.__setitem__(key, value)
    
    def __setitem__(self, key, value):
        super(APIObject, self).__setitem__(key, convert_to_APIObject(value))
        self.__dict__.update({key: convert_to_APIObject(value)})
        
    def __delattr__(self, item):
        self.__delitem__(item)
        
    def __delitem__(self, key):
        super(APIObject, self).__delitem__(key)
        del self.__dict__[key]
        
    def update(self, dict_obj):
        super(APIObject, self).update(dict_obj)        
        for k, v in dict_obj.iteritems():
            self[k] = convert_to_APIObject(v)
        
class APIResource(APIObject):
    
    def request(self, method, auth_obj, api_group, api_version, api_path, headers, params, 
                post_data):
        req = requestor.Requestor(auth_obj)
        return req.request(method, api_group, api_version, api_path, headers, params, post_data)

