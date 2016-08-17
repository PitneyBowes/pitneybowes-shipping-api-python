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
# File: transactonreport_test.py
# Description: transaction report management related tests
#

import json
import unittest
import test_util
from pbshipping import *

class TestTransactionReport(unittest.TestCase):

    def setUp(self):
        test_util.setup_env()        
        self.auth_obj = AuthenticationToken(api_key=test_util._test_api_key, 
                                            api_secret=test_util._test_api_secret)

    def tearDown(self):
        pass

    def testTransactionReport(self):
        print "Testing get transaction report  ..."        
        Developer(developerid=test_util._test_devid).getTransactionReport(
            self.auth_obj, None)


if __name__ == "__main__":
    unittest.main()