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
# File: mainfest_test.py
# Description: manifest management related tests
#

import datetime
import unittest
import test_util
from pbshipping import *

class TestManifest(unittest.TestCase):

    def setUp(self):
        test_util.setup_env()        
        self.auth_obj = AuthenticationToken(api_key=test_util._test_api_key, 
                                            api_secret=test_util._test_api_secret)
        self.developer = test_util.setup_developer(self.auth_obj)
        merchant, acct_num = test_util.setup_merchant(self.auth_obj, self.developer)
        self.shipper_id = merchant.postalReportingNumber

    def tearDown(self):
        pass

    def testManifest(self):
        shipment1, txid1 = test_util.create_single_shipment(
            self.auth_obj, self.developer, self.shipper_id)
        shipment2, txid2 = test_util.create_single_shipment(
            self.auth_obj, self.developer, self.shipper_id)
        trk_nums = [shipment1.parcelTrackingNumber, 
                    shipment2.parcelTrackingNumber]
        manifest = Manifest(
            carrier=test_util._MY_RATE_REQUEST_CARRIER_USPS["carrier"], 
            submissionDate=datetime.datetime.utcnow().strftime("%Y-%m-%d"),
            parcelTrackingNumbers=trk_nums,
            fromAddress=shipment1.fromAddress)
        txid = test_util.get_pb_tx_id()

        print "Testing manifest creation ..."
        manifest.create(self.auth_obj, txid)
        self.assertEqual("manifestId" in manifest, True)
                        
        print "Testing reprint manifest ..."
        manifest.reprint(self.auth_obj)
        
        print "Testing retry manifest ..."
        manifest.retry(self.auth_obj, test_util.get_pb_tx_id(), txid)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()