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
# File: shipment_test.py
# Description: shipment management related tests
#

import unittest
import test_util
from pbshipping import *

class TestShipment(unittest.TestCase):

    def setUp(self):
        test_util.setup_env()
        self.auth_obj = AuthenticationToken(api_key=test_util._test_api_key, 
                                            api_secret=test_util._test_api_secret)

        developer = Developer(developerid=test_util._test_devid)
        merchant = developer.registerMerchantIndividualAccount(self.auth_obj, 
            test_util._test_merchant_email)
        self.shipper_id = merchant.postalReportingNumber

    def tearDown(self):
        pass

    def testShipment(self):
        rate = Rate(test_util._MY_RATE_REQUEST_CARRIER_USPS)  
        parcel = Parcel(test_util._MY_PARCEL)              
        shipment = Shipment(fromAddress=test_util._MY_ORIGIN_ADDR, 
                            toAddress=test_util._MY_DEST_ADDR,
                            parcel=parcel, rates=[rate])
        
        print "Testing get shipment rates ..."
        rates = shipment.getRates(self.auth_obj, test_util.get_pb_tx_id(), True)  
    
        shipment.rates = rates    
        shipment.documents = [Document(test_util._MY_SHIPMENT_DOCUMENT)]
        shipment.shipmentOptions = [
            ShipmentOptions({"name": "SHIPPER_ID", "value": self.shipper_id}),
            ShipmentOptions({"name": "ADD_TO_MANIFEST", "value": "true" })
        ]
        txid = test_util.get_pb_tx_id()
        
        print "Testing purchase shipment label ..."
        shipment.createAndPurchase(self.auth_obj, txid, True)
        self.assertEqual("shipmentId" in shipment, True)
        
        tracking = Tracking(trackingNumber=shipment.parcelTrackingNumber)
        try:
            print "Testing get tracking status ..."
            tracking.updateStatus(self.auth_obj)        
        except APIError, api_err:
            if len(api_err.error_info) < 1:
                raise api_err
            if api_err.error_info[0]["errorCode"] != 'PB-TRKPKG-ERR-7600':
                raise api_err
            print "   get tracking call not successful ..."
            print "   this is normal if you are running in sandbox environment"
            print "   since it is expected there is no real tracking number"
                    
        print "Testing reprint shipment label ..."
        shipment.reprintLabel(self.auth_obj)
        
        print "Testing retry shipment ..."
        Shipment.retryByTransactionId(self.auth_obj, test_util.get_pb_tx_id(), 
                                      txid)
    
        print "Testing canceling shipment ..."
        cancel_result = shipment.cancel(self.auth_obj, test_util.get_pb_tx_id(), 
                              shipment.rates[0].carrier)
        self.assertEqual("status" in cancel_result, True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()