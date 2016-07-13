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
# File: __init__.py
# Description: initialization and configuration administration logic
#

# Shippging API runtime configuration with Defaults
# - this contains environment configurations and well-defined 
#   keywords to be used in Shipping APIs. 
# - params contains configurable environment related parameters
#   - "sandbox": URL to Pitney Bowes shipping services sandbox server
#   - "production": URL to Pitney Bowes shipping services production serve 
#   - "is_production": points to production server when set to true, 
#                      sandbox server when set to false.
#   - 'default_api_version": version number to be used for all API calls
#     unless there is an explicit override configured.
#   - 'override_api_version": a Python dictionary object containing specific
#     API version overwriting information 
#     consult the comment block for each method in shipping_resource.py 
#     for the API signature for each REST call.
#
class Configuration: 
    params = {
        "sandbox": "https://api-sandbox.pitneybowes.com",
        "production": "https://api.pitneybowes.com",
        "is_production": False,
        "default_api_version": "/v1",
        "override_api_version": {
            "post/developers/.../merchants/registration": "/v2",
            "get/ledger/developers/.../transactions/reports": "/v2"
        }
    }
    api_group_shipping = '/shippingservices'
    txid_attrname = "X-PB-TransactionId"    

from authentication import *
from error import *
from resource import *
from shipping_resource import *

