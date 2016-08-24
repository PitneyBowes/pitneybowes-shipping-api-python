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
# Description: supporting classes for test suite
#

import sys
sys.path.insert(0, "../")
sys.path.insert(0, "../../")
import os
import time
import datetime
import json
from decimal import Decimal
from pbshipping import *

_test_api_key=None # <set here or through env variable PBSHIIPING_KEY
_test_api_secret=None # <set here or through env variable PBSHIPPING_SECRET
_test_devid=None # <set here or through env variable PBSHIPPING_DEVID
_test_merchant_email=None # <set here or through env variable PBSHIPPING_MERCHANT
_test_sandbox=None # <set here or through env variable PBSHIPPING_SANDBOX
_test_production=None # <set here or through env variable PBSHIPPING_PRODUCTION
_test_is_production=None # <set here or through env variable PBSHIPPING_IS_PRODUCTION

_MY_BULK_MERCHANT_ADDR = {
    "addressLines" : ["27 Waterview Drive"], 
    "cityTown" : "Shelton",
    "stateProvince" : "Connecticut",
    "postalCode" : "06484",
    "countryCode" : "US",
    "company" : "Pitney Bowes",
    "name": "John Doe",
    "email" : "dummy@pbshipping.com", 
    "phone": "203-792-1600",
    "residential": False
}

_MY_ORIGIN_ADDR = {
    "addressLines" : ["37 Executive Drive"], 
    "cityTown" : "Danbury",
    "stateProvince" : "Connecticut",
    "postalCode" : "06810",
    "countryCode" : "US"
}

_MY_DEST_ADDR = {
    "addressLines" : ["27 Waterview Drive"], 
    "cityTown" : "Shelton",
    "stateProvince" : "Connecticut",
    "postalCode" : "06484",
    "countryCode" : "US"
}
   
_MY_PARCEL = {
    "weight": {
        "unitOfMeasurement":"OZ",
        "weight":1
    },
    "dimension":{
        "unitOfMeasurement":"IN",
        "length":6,
        "width":0.25,
        "height":4,
        "irregularParcelGirth":0.002
    }
}

_MY_RATE_REQUEST_CARRIER_USPS = {
    "carrier":"usps",
    "serviceId":"PM",
    "parcelType":"PKG",
    "specialServices": [
        {
            "specialServiceId":"Ins",
            "inputParameters" : [
                {
                    "name" : "INPUT_VALUE",
                    "value" : "50"
                }
             ]
        },
        {
            "specialServiceId":"DelCon",
            "inputParameters" : [
                {
                    "name" : "INPUT_VALUE",
                    "value" : "0"
                }
             ]
        }
    ],
    "inductionPostalCode":"06810"
}

_MY_SHIPMENT_DOCUMENT = {
    "type": "SHIPPING_LABEL",
    "contentType": "URL",
    "size": "DOC_8X11",
    "fileFormat": "PDF",
    "printDialogOption": "NO_PRINT_DIALOG"
}

# retrieve configurable environment paramteres
def setup_env():
    global _test_api_key, _test_api_secret, _test_devid, _test_merchant_email
    global _test_sandbox, _test_production, _test_is_production
    
    if _test_api_key is None:
        _test_api_key = os.environ.get("PBSHIPPING_KEY", None)
    if _test_api_secret is None:
        _test_api_secret = os.environ.get("PBSHIPPING_SECRET", None)
    if _test_devid is None:
        _test_devid = os.environ.get("PBSHIPPING_DEVID", None)
    if _test_merchant_email is None:
        _test_merchant_email = os.environ.get("PBSHIPPING_MERCHANT", None)
    if _test_sandbox is None:
        _test_sandbox = os.environ.get("PBSHIPPING_SANDBOX", None)
    if _test_production is None:
        _test_production = os.environ.get("PBSHIPPING_PRODUCTION", None)
    if _test_is_production is None:
        str_is_production = os.environ.get("PBSHIPPING_IS_PRODUCTION", "false")
        str_is_production = str_is_production.lower()
        if str_is_production == "false":
            _test_is_production = False
        else:
            _test_is_production = True

    if _test_sandbox is not None:
        Configuration.params["sandbox"] = _test_sandbox
    if _test_production is not None:
        Configuration.params["production"] = _test_production
    if _test_is_production is not None:
        Configuration.params["is_production"] = _test_is_production

# this helps to identify transactions originating from the test suite
_TEST_SUITE_TXID_PREFIX = "KYCB"
# generate a unique transaction id        
def get_pb_tx_id():
    time_now = datetime.datetime.utcnow()
    return _TEST_SUITE_TXID_PREFIX + time_now.strftime("%Y%m%d%H%M%S%f")

# set up developer record 
def setup_developer(auth_obj):
    developer = Developer(developerid=_test_devid);
    # need this to retrieve developers attributes
    developer.refresh(auth_obj)
    return developer

# set up the merchant according to environment setting
def setup_merchant(auth_obj, developer):
    if developer.bulkMode == False:
        # individual account mode
         merchant = developer.registerMerchantIndividualAccount(
            auth_obj, _test_merchant_email)
         acct_num = merchant.paymentAccountNumber
    else:
        # bulk account mode
        # since we are given merchant credential for individual account mode
        # we expect to fail with Invalid developer type
        try:
            raw_addr = _MY_BULK_MERCHANT_ADDR
            raw_addr["email"] = _test_merchant_email
            merchant = developer.registerMerchantBulkAccount(
                auth_obj, Address(raw_addr))
        except APIError, api_err:
            if len(api_err.error_info) < 1: 
                raise api_err
            if "Duplicate entry" not in api_err.error_info[0]['message']:
                raise api_err
            merchant = developer.getMerchantBulkAccount(
                auth_obj, _test_merchant_email)
        acct_num = developer.paymentAccount
    return merchant, acct_num
    
# return the shipment rate used in the test suite for reference
def check_shipment_rate(auth_obj, developer):
    xtra_hdrs = None
    if developer.bulkMode == True and developer.useShipperRate == True:
        xtra_hdrs = {"X-PB-Shipper-Rate-Plan": "PP_SRP_NEWBLUE"}

    shipment = Shipment(fromAddress=_MY_ORIGIN_ADDR, 
                        toAddress=_MY_DEST_ADDR,
                        parcel=Parcel(_MY_PARCEL), 
                        rates=[Rate(_MY_RATE_REQUEST_CARRIER_USPS)])                
    rates = shipment.getRates(auth_obj, get_pb_tx_id(), True, xtra_hdrs)  
    return rates[0].totalCarrierCharge   

# create a single shipment and purchase a label    
def create_single_shipment(auth_obj, developer, shipper_id):
 
    xtra_hdrs = None
    if developer.bulkMode == True and developer.useShipperRate == True:
        xtra_hdrs = {"X-PB-Shipper-Rate-Plan": "PP_SRP_NEWBLUE"}

    shipment = Shipment(fromAddress=_MY_ORIGIN_ADDR, 
                        toAddress=_MY_DEST_ADDR,
                        parcel=Parcel(_MY_PARCEL), 
                        rates=[Rate(_MY_RATE_REQUEST_CARRIER_USPS)],
                        documents = [Document(_MY_SHIPMENT_DOCUMENT)])
    shipment.shipmentOptions = [
        ShipmentOptions({"name": "SHIPPER_ID", "value": shipper_id}),
        ShipmentOptions({"name": "ADD_TO_MANIFEST", "value": "true" })
    ]
    txid = get_pb_tx_id()
    shipment.createAndPurchase(auth_obj, txid, True, xtra_hdrs) 
    
    return shipment, txid

# verify the ledger balance is correct after shipment label purchase
def verify_ledger_balance_after_txn(shipment, start_balance, end_balance):

    balance_delta = start_balance.balance - end_balance.balance
    # if account has been replenished using auto-refill, skip this case
    if balance_delta < 0:
        print "    ending balance increases, probably due to auto reload, skip check"
        return True
    
    txn_charge = shipment.rates[0].totalCarrierCharge
    is_same = (txn_charge == balance_delta)
    if is_same == False:
        msg = "    verify balance failed: difference is " 
        msg += str(txn_charge - balance_delta)
        print msg

    return is_same
    
    
    
    
    
    
