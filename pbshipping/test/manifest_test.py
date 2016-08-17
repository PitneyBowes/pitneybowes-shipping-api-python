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
        
        developer = Developer(developerid=test_util._test_devid)
        merchant = developer.registerMerchantIndividualAccount(self.auth_obj, 
            test_util._test_merchant_email)
        shipper_id = merchant.postalReportingNumber
                
        rate = Rate(test_util._MY_RATE_REQUEST_CARRIER_USPS)  
        parcel = Parcel(test_util._MY_PARCEL)    
                  
        self.shipment1 = Shipment(fromAddress=test_util._MY_ORIGIN_ADDR, 
                            toAddress=test_util._MY_DEST_ADDR,
                            parcel=parcel, rates=[rate])
        self.shipment2 = Shipment(fromAddress=test_util._MY_ORIGIN_ADDR, 
                            toAddress=test_util._MY_DEST_ADDR,
                            parcel=parcel, rates=[rate])
                
        rates = self.shipment1.getRates(self.auth_obj, 
                                        test_util.get_pb_tx_id(), True)      
        self.shipment1.rates = rates    
        self.shipment1.documents = [Document(test_util._MY_SHIPMENT_DOCUMENT)]
        self.shipment1.shipmentOptions = [
            ShipmentOptions({"name": "SHIPPER_ID", "value": shipper_id}),
            ShipmentOptions({"name": "ADD_TO_MANIFEST", "value": "true" })
        ]
        
        rates = self.shipment2.getRates(self.auth_obj, 
                                        test_util.get_pb_tx_id(), True)      
        self.shipment2.rates = rates    
        self.shipment2.documents = [Document(test_util._MY_SHIPMENT_DOCUMENT)]
        self.shipment2.shipmentOptions = [
            ShipmentOptions({"name": "SHIPPER_ID", "value": shipper_id}),
            ShipmentOptions({"name": "ADD_TO_MANIFEST", "value": "true" })
        ]
        
        self.shipment1.createAndPurchase(self.auth_obj, 
                                         test_util.get_pb_tx_id(), True) 
        self.shipment2.createAndPurchase(self.auth_obj,
                                         test_util.get_pb_tx_id(), True)
        
    def tearDown(self):
        self.shipment1.cancel(self.auth_obj, test_util.get_pb_tx_id(), 
                              self.shipment1.rates[0].carrier)
        self.shipment2.cancel(self.auth_obj, test_util.get_pb_tx_id(), 
                              self.shipment2.rates[0].carrier)        

    def testManifest(self):
        trk_nums = [self.shipment1.parcelTrackingNumber, 
                    self.shipment2.parcelTrackingNumber]
        manifest = Manifest(
            carrier=test_util._MY_RATE_REQUEST_CARRIER_USPS["carrier"], 
            submissionDate=datetime.datetime.utcnow().strftime("%Y-%m-%d"),
            parcelTrackingNumbers=trk_nums,
            fromAddress=self.shipment1.fromAddress)
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