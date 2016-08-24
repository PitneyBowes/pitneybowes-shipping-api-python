#!/usr/bin/python
# -*- coding: utf-8 -*-

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
# File: tutorial_client_library.py
# Description: a tutorial that walks through the shipping work flow and include
#              all available client library calls and corresponding 
#              documentation.
#

import time, datetime, getopt, sys, os
from pbshipping import *

_api_key = None
_api_secret = None
_dev_id = None 
_merchant_email = None
_merchant = None
_from_addr = None
_to_addr = None
_shipment = None
_shipment_orig_tx_id = None
_tracking = None
_manifest = None
_manifest_orig_tx_id = None
_auth_obj = None

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

    
# use the current timestamp to generate a transaction id 
def get_pb_tx_id():
    return datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f")

# obtain authentication, developer, and merchant infomratoin from 
# command line
def initialize_info():
    
    global _api_key, _api_secret, _dev_id, _merchant_email
    
    # make sure we obtain the necessary developer and merchant information
    # from the command line arguments
    optlist = getopt.getopt(sys.argv[1:], "h", 
                            ["key=", "secret=", "devid=", "merchant="])
    optdict = dict(optlist[0])
    
    cmdline_syntax = "--key=<api key value> "
    cmdline_syntax += "--secret=<api secret value> "
    cmdline_syntax += "--devid=<developer id> "
    cmdline_syntax += "--merchant=<merchant registered email address>"
    
    # try getting through environment variables first
    _api_key = os.environ.get("PBSHIPPING_KEY", None)
    _api_secret = os.environ.get("PBSHIPPING_SECRET", None)
    _dev_id = os.environ.get("PBSHIPPING_DEVID", None)
    _merchant_email = os.environ.get("PBSHIPPING_MERCHANT", None) 
                            
    if "--key" not in optdict:
        if _api_key is None:
            print "main: missing developer key information"
            print "main: command line arguments " + cmdline_syntax
            sys.exit(1)
    else:
        _api_key = optdict["--key"]
    if "--secret" not in optdict:
        if _api_secret is None:
            print "main: missing developer secret information"
            print "main: command line arguments " + cmdline_syntax
            sys.exit(1)
    else:
        _api_secret = optdict["--secret"]              
    if "--devid" not in optdict: 
        if _dev_id is None:
            print "main: missing developer ID information"
            print "main: command line arguments " + cmdline_syntax
            sys.exit(1)
    else:
        _dev_id = optdict["--devid"]
    if "--merchant" not in optdict:
        if _merchant_email is None:
            print "main: missing developer associated merchant information"
            print "main: command line arguments " + cmdline_syntax 
            sys.exit(1)
    else:
        _merchant_email = optdict["--merchant"]    

# choose sandbox or production pitney bowes shipping api server
def choose_environment():
    
    print "Choose the sandbox environment ..."
    Configuration.params["is_production"] = False

# authenticate and obtain the authentication object for subsequent use
# underlying API: POST /oauth/token
def authenticate():
    
    global _auth_obj

    print "Authenticating ..."
    _auth_obj = AuthenticationToken(api_key=_api_key, api_secret=_api_secret)

# return the list of supported countries 
# underlying API: GET /countries
def check_carrier_supported_countries():
    
    print "Querying for supported countries of USPS carrier ..."
    usps_carrier = Carrier({"name": "usps"})
    supported_countries = usps_carrier.getCountries(_auth_obj, "US")
    n = len(supported_countries)
    print "   number of supported countries is " + str(n)
    print "   one example is " +  supported_countries[n/3].countryName

# managing merchant account under individual account mode
# underlying API: GET /developers/{developerId}/merchants/emails/{emailId}/
#                 GET /ledger/accounts/{accountNumber}/balance
def manage_individual_mode_merchant():
    
    global _merchant
    
    # querying for merchant information
    print "Managing merchant (individual account mode) ..."
    developer = Developer(developerid=_dev_id)
    _merchant = developer.registerMerchantIndividualAccount(_auth_obj, 
                                                            _merchant_email)
    merchant_account_number = _merchant.paymentAccountNumber
    
    # querying for merchant account balance
    balance = Account.getBalanceByAccountNumber(_auth_obj, 
                                                merchant_account_number)
    print "   merchant full name is " + _merchant.fullName
    print "   shipper id is " + _merchant.postalReportingNumber
    print "   payment account number is " + merchant_account_number
    print "   current balance is " + balance.currencyCode + " " + \
                                     str(balance.balance)

# managing merchant account under bulk account mode
# underlying API: POST /developers/{developerId}/merchants/registration
def manage_bulk_mode_merchant():
    print "Managing merchant (bulk account mode) ..."
    
    developer = Developer(developerid=_dev_id)
    merchant_addr = Address(_MY_BULK_MERCHANT_ADDR)
    merchant = developer.registerMerchantBulkAccount(_auth_obj, merchant_addr)
    print merchant

# verifying addresses
# underlying API: POST /addresses/verify
def verify_addresses():
    
    global _from_addr, _to_addr
    
    print "Verifying origin and destination addresses ... "
    _from_addr = Address(_MY_ORIGIN_ADDR)
    _from_addr.verify(_auth_obj, False)
    if _from_addr.status.lower() == "validated_changed":
        print "   origin address cleansed, addressLine is " + \
              _from_addr.addressLines[0]

    _to_addr = Address(_MY_DEST_ADDR)
    _to_addr.verify(_auth_obj, False)
    if _to_addr.status.lower() == "validated_changed":
        print "   destination address cleansed, addressLine is " + \
              _to_addr.addressLines[0]        

# querying rates to prepare a shipment
# underlying API: POST /rates
def prepare_shipment():
    
    global _shipment
    
    print "Checking for shipment rates ..."
    rate = Rate(_MY_RATE_REQUEST_CARRIER_USPS)  
    parcel = Parcel(_MY_PARCEL)              
    _shipment = Shipment(fromAddress=_from_addr, toAddress=_to_addr,
                         parcel=parcel, rates=[rate])
    rates = _shipment.getRates(_auth_obj, get_pb_tx_id(), True)  
    print "   total carrier charge: " + str(rates[0].totalCarrierCharge)
    
    print "Now preparing shipment ..."
    _shipment.rates = rates    
    _shipment.documents = [Document(_MY_SHIPMENT_DOCUMENT)]
    _shipment.shipmentOptions = [
        ShipmentOptions({"name": "SHIPPER_ID", 
                         "value": _merchant.postalReportingNumber}),
        ShipmentOptions({"name": "ADD_TO_MANIFEST", 
                         "value": "true" })
    ]
    return _shipment

# submit a shipment creation request and purchase a shipment label
# underlying API: POST /shipments
def create_and_purchase_shipment():
    
    global _shipment_orig_tx_id
    
    print "Creating shipment and purchasing label ..."
    _shipment_orig_tx_id = get_pb_tx_id()
    _shipment.createAndPurchase(_auth_obj, _shipment_orig_tx_id, True)
    print "   parcel tracking number is " + _shipment.parcelTrackingNumber
    for doc in _shipment.documents:
        print "   document type is " + doc["type"]
        if doc["contentType"] == "URL" and "contents" in doc:
            print "   document URL is " + doc["contents"]

# reprint a shipment label
# underlying API: GET /shipments/{shipmentId}
def reprint_shipment():
    
    print "Reprinting label ..."
    _shipment.reprintLabel(_auth_obj)
    for doc in _shipment.documents:
        if doc["contentType"] == "URL" and "contents" in doc:
            print "   document URL is " + doc["contents"]        

# retry a shipment purchase request 
# underlying API: GET /shipments?originalTransactionId    
def retry_shipment():
    
    print "Retrying shipment order ..."
    _shipment.retry(_auth_obj, get_pb_tx_id(),  _shipment_orig_tx_id)
 
# submit a shipment cancellation request
# underlying API: DELETE /shipments/{shipmentId}
def cancel_shipment():
    
    print "Canceling shipment order ..." 
    cancel_result = _shipment.cancel(_auth_obj, get_pb_tx_id(), 
                                      _shipment.rates[0].carrier)
    print "   status: " + cancel_result["status"]

# create a manifest
# underlying API: POST /manifests
def create_manifest():
    
    global _manifest, _manifest_orig_tx_id

    print "Creating manifest ..."
    _manifest = Manifest(carrier=_tracking.carrier, 
                         submissionDate=datetime.datetime.utcnow().strftime("%Y-%m-%d"),
                         parcelTrackingNumbers=[_shipment.parcelTrackingNumber],
                         fromAddress=_shipment.fromAddress)
    _manifest_orig_tx_id = get_pb_tx_id()
    _manifest.create(_auth_obj, _manifest_orig_tx_id)
    print "   manifest tracking number is " + _manifest.manifestTrackingNumber
    print "   manifest id is " + _manifest.manifestId

# reprint a manifest
# underlying API: GET /manifests/{manifestId}
def reprint_manifest():
    
    print "Repringing manifest ..."
    _manifest.reprint(_auth_obj)
    print "   reprinted manifestId is " + _manifest.manifestId

# retry a mainfest
# Underly API: GET /manifests
def retry_manifest():
    
    print "Retrying manifest request ..."
    _manifest.retry(_auth_obj, get_pb_tx_id(), _manifest_orig_tx_id)   
    print "   manifest id is " + _manifest.manifestId

# get tracking information
# Underlying API: GET /tracking/{trackingNumber}
def get_tracking_update():
    
    global _tracking
    
    print "Get tracking status ..."
    _tracking = Tracking(trackingNumber=_shipment.parcelTrackingNumber)
    try:
        _tracking.updateStatus(_auth_obj)        
    except APIError, api_err:
        if Configuration.params["is_production"] == False:
                print "   no tracking information in sandbox environment"
                return
        raise api_err

    print "   status = " + _tracking.status

# querying for a transaction report
# Underlying API: GET /ledger/developers/{developerId}/transactions/reports
def get_transaction_report():
    
    print "Retrieving transaction report ..."
    params = dict()
    params["merchantId"] = _merchant.postalReportingNumber
    report = Developer(developerid=_dev_id).getTransactionReport(_auth_obj, params)
    for next_row in report.content:
        txn = TransactionDetails(next_row)
        txn_detail = "      id: " + txn.transactionId
        txn_detail += " type: " + txn.transactionType
        print txn_detail

def main():
    try:
        initialize_info()        
        
        choose_environment()
        
        authenticate()
        
        check_carrier_supported_countries()
        
        # choose appropriate calls for individual or bulk account mode
        manage_individual_mode_merchant()
        # manage_bulk_mode_merchant()

        verify_addresses()
        prepare_shipment()
        create_and_purchase_shipment()
        reprint_shipment()
        retry_shipment()

        get_tracking_update()        
        
        create_manifest()
        reprint_manifest()
        retry_manifest()
        
        get_transaction_report()
        
        cancel_shipment()
        
    except Exception, e:
        if isinstance(e, AuthenticationError) or isinstance(e, APIError):
            print str(e.http_status) + " " + str(e.message)
            print e.error_info
        else:
            print "hit an exception"
            print e

if __name__ == '__main__':
    main()
