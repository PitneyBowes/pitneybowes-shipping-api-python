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
# File: merchant_test.py
# Description: merchant management related tests
#

import unittest
import test_util
from pbshipping import *

class TestMerchant(unittest.TestCase):

    def setUp(self):
        test_util.setup_env()
        self.auth_obj = AuthenticationToken(api_key=test_util._test_api_key, 
                                            api_secret=test_util._test_api_secret)

    def tearDown(self):
        pass

    def testMerchant(self):
        developer = Developer(developerid=test_util._test_devid)
        
        # individual account mode        
        print "Testing merchant registration (individual account mode) ..."
        merchant = developer.registerMerchantIndividualAccount(self.auth_obj, 
            test_util._test_merchant_email)
        acct_num = merchant.paymentAccountNumber
                
        # bulk account mode
        # since we are given merchant credential for individual account mode
        # we expect to fail with Invalid developer type
        print "Testing merchant registration (bulk account mode) ..."
        try:
            merchant2 = developer.registerMerchantBulkAccount(self.auth_obj, 
                Address(test_util._MY_BULK_MERCHANT_ADDR))
        except APIError, api_err:
            if len(api_err.error_info) < 1: 
                raise api_err
            if api_err.error_info[0]["message"] != "Invalid developer type!":
                raise api_err
            print "   bulk mode merchant registration call fails"
            print "   but this can be normal if the developer is not configured"
            print "   for bulk account mode"
     
        print "Testing account balance query ..."
        Account.getBalanceByAccountNumber(self.auth_obj, acct_num)

if __name__ == "__main__":
    unittest.main()