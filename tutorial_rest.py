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
# File: tutorial_rest.py
# Description: a tutorial that walks through the shipping work flow using
#              the shipping REST API directly. 
#

import sys
import os
import getopt
import base64
import time
import json
import urlparse
import urllib
import urllib2

#-------------------------------------------------------------------------------
# Constants
#-------------------------------------------------------------------------------
_PB_SHIPPINGAPI_SANDBOX = 'https://api-sandbox.pitneybowes.com'
_PB_SHIPPINGAPI_BASEPATH = '/shippingservices/v1'

_MY_ORIGIN_ADDR = {
    "addressLines" : ["37 Executive Dr"], 
    "cityTown" : "Danbury",
    "stateProvince" : "Connecticut",
    "postalCode" : "06810",
    "countryCode" : "US"
}

_MY_DEST_ADDR = {
    "addressLines" : ["27 Waterview Dr"], 
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
    "inductionPostalCode":"06484"
}

_MY_SHIPMENT_DOCUMENT = {
    "type": "SHIPPING_LABEL",
    "contentType": "URL",
    "size": "DOC_8X11",
    "fileFormat": "PDF",
    "printDialogOption": "NO_PRINT_DIALOG"
}

_TIME_FMT = '%Y-%m-%dT%H:%M:%SZ'

#-------------------------------------------------------------------------------
# Globals
#-------------------------------------------------------------------------------
_pb_server = _PB_SHIPPINGAPI_SANDBOX
_pb_oauth_params = None

def utf8(value):
    if isinstance(value, unicode) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    else:
        return value

def encode_dict_utf8(dict_obj):
    for key, value in dict_obj.iteritems():
        key = utf8(key)
        yield (key, utf8(value))

def construct_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)

    if base_query:
        query = '%s&%s' % (base_query, query)

    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))

#-------------------------------------------------------------------------------
# urllib2_request_with_method
# - subclass urllib2 class to support all 4 HTTP methods (POST/PUT/GET/DELETE) 
#-------------------------------------------------------------------------------
class urllib2_request_with_method(urllib2.Request):
    def __init__(self, method, *args, **kwargs):
        self._method = method
        urllib2.Request.__init__(self, *args, **kwargs)
        
    def get_method(self):
        return self._method
    
#-------------------------------------------------------------------------------
# call_shipping_api
# - make a REST shipping API call; 
# - the request header will be set accordingly depending on the HTTP method; 
# - the request data is expected to be in JSON format
# - on successful invocation, a result dictionary object will be returned:
#   - 'status_code': HTTP code returned from the rest call
#   - 'type': response data content type as found in the response header
#   - 'data': response data as JSON object 
# - exception should be raised on HTTP level error or other exceptions 
#   encountered during the execution
#-------------------------------------------------------------------------------    
def call_shipping_api(api_path, http_method, req_xtr_hdrs, req_params, req_data):

    req_headers = {"Authorization" : _pb_oauth_params}  
    if (http_method != "GET"):
        req_headers["Content-Type"] = "application/json"     
    if req_xtr_hdrs != None:
        req_headers.update(req_xtr_hdrs)    

    url = _pb_server + _PB_SHIPPINGAPI_BASEPATH + api_path
    if req_params != None and len(req_params) > 0:
        encoded_params = urllib.urlencode(list(encode_dict_utf8(req_params)))
        url = construct_api_url(url, encoded_params)

    if http_method is "GET" or req_data is None:
        req_data_str = ""
    else:
        req_data_str = json.dumps(req_data) 

    print "call_shipping_api with url: " + url
    
    req = urllib2_request_with_method(http_method, url, req_data_str, req_headers)
    resp = urllib2.urlopen(req)

    status_code = resp.getcode() 
    content_type = resp.info().getheader('Content-Type')
    content = resp.read()
        
    # prepare result object, would need to deserialize JSON response data
    result = dict()
    result['status_code'] = status_code
    result['type'] = content_type
    if (result['type'].startswith('application/json') == True):
        result['data'] = json.loads(content)
    else:    
        result['data'] = content
        
    return result

#-------------------------------------------------------------------------------
# generate_pb_txid
# - generate a PB Transaction ID for per transaction use
#-------------------------------------------------------------------------------
def getPbTxId():
    return str(int(time.time()))

#-------------------------------------------------------------------------------
# authorize_and_authenticate
# - first rest call to obtain OAuth token to be used throughout the session
#-------------------------------------------------------------------------------
def authenticate_and_authorize(api_key, api_secret):
    auth_encoded = base64.b64encode(api_key + ':' + api_secret)
    req_headers = {"Content-Type" : "application/x-www-form-urlencoded", 
                   "Authorization" : "Basic " + auth_encoded }
    req_data = dict()
    req_data['grant_type'] = 'client_credentials'
    url = _pb_server + '/oauth/token'
    
    post_data_str = urllib.urlencode(list(encode_dict_utf8(req_data)))
    
    req = urllib2_request_with_method("POST", url, post_data_str, req_headers) 
    resp = urllib2.urlopen(req)

    global _pb_oauth_params
    oauth_obj = json.loads(resp.read())
    
    _pb_oauth_params = u"Bearer " + oauth_obj["access_token"]

#-------------------------------------------------------------------------------
# main 
#-------------------------------------------------------------------------------

def main():

    try:
        # make sure we obtain the necessary developer and merchant information
        # from the command line arguments
        optlist = getopt.getopt(sys.argv[1:], "h", ["key=", "secret=", 
                                                   "devid=", "merchant="])
        optdict = dict(optlist[0])
        cmdline_syntax = "--key=<api key value> "
        cmdline_syntax += "--secret=<api secret value> "
        cmdline_syntax += "--devid=<developer id> "
        cmdline_syntax += "--merchant=<merchant registered email address "
        
        if "-h" in optdict:
            print "main: command line arguments " + cmdline_syntax
            sys.exit(1)

        # try getting through environment variables first
        api_key = os.environ.get("PBSHIPPING_KEY", None)
        api_secret = os.environ.get("PBSHIPPING_SECRET", None)
        dev_id = os.environ.get("PBSHIPPING_DEVID", None)
        merchant_email = os.environ.get("PBSHIPPING_MERCHANT", None) 
                            
        if "--key" not in optdict:
            if api_key is None:
                print "main: missing developer key information"
                print "main: command line arguments " + cmdline_syntax
                sys.exit(1)
        else:
            api_key = optdict["--key"]
        if "--secret" not in optdict:
            if api_secret is None:
                print "main: missing developer secret information"
                print "main: command line arguments " + cmdline_syntax
                sys.exit(1)
        else:
            api_secret = optdict["--secret"]              
        if "--devid" not in optdict: 
            if dev_id is None:
                print "main: missing developer ID information"
                print "main: command line arguments " + cmdline_syntax
                sys.exit(1)
        else:
            dev_id = optdict["--devid"]
        if "--merchant" not in optdict:
            if merchant_email is None:
                print "main: missing developer associated merchant information"
                print "main: command line arguments " + cmdline_syntax 
                sys.exit(1)
        else:
            merchant_email = optdict["--merchant"]        
     
        # STEP 1: authenticate and authorize using the given key and secret to 
        #         obtain an OAuth token to be used throughout the session
        authenticate_and_authorize(api_key, api_secret)
        
        # STEP 2: manipulate and verify shipping address
        
        # check if United States is supported as destination through the 
        # GetCountry API
        req_params = dict()
        req_params["carrier"] = "usps"
        req_params["originCountryCode"] = "US"       
        result = call_shipping_api("/countries", "GET", None, req_params, None) 
        if any(d['countryCode'] == 'US' for d in result["data"]):
            print "US is supported as destination"
        else:
            print "US is NOT supported as destination"

        # verify this example origin and destination addresses 
        req_hdrs = dict()
        req_hdrs["minimalAddressValidation"] = False
        req_data = _MY_ORIGIN_ADDR
        result = call_shipping_api("/addresses/verify", "POST", req_hdrs, None, req_data)    
        cleansed_origin_addr = result["data"]
        req_data = _MY_DEST_ADDR
        result = call_shipping_api("/addresses/verify", "POST", req_hdrs, None, req_data)
        cleansed_dest_addr = result["data"]
    
        # STEP 3: obtain merchant account information  (in individual account model) 
        api_path = "/developers/" + dev_id + "/merchants/emails/" + urllib.quote_plus(utf8(merchant_email)) + "/"
        result = call_shipping_api(api_path, "GET", None, None, None)
        merchant_record = result['data']
        
        # STEP 4: query merchant's ledger balance
        api_path = "/ledger/accounts/" + urllib.quote_plus(utf8(merchant_record['paymentAccountNumber'])) + "/balance"
        result = call_shipping_api(api_path, "GET", None, None, None) 
        print "merchant " + merchant_record["paymentAccountNumber"] + " current balance is " + str(result["data"])
            
        # STEP 5: look up shipping rates
        req_hdrs = dict()
        req_hdrs["X-PB-TransactionId"] = getPbTxId() # next transaction id
        req_params = dict()
        req_params["includeDeliveryCommitment"] = True
        req_data = dict()
        req_data["fromAddress"] = cleansed_origin_addr
        req_data["toAddress"] = cleansed_dest_addr
        req_data["parcel"] = _MY_PARCEL
        req_data["rates"] = [_MY_RATE_REQUEST_CARRIER_USPS]
        result = call_shipping_api('/rates', "POST", req_hdrs, req_params, req_data)
        given_rates = result["data"]["rates"]
        
        # STEP 6: create a shipment 
        req_hdrs = dict()
        req_hdrs["X-PB-TransactionId"] = getPbTxId() # next transaction id      
        req_params = dict()
        req_params["includeDeliveryCommitment"] = True
        req_data = dict()
        req_data["fromAddress"] = cleansed_origin_addr
        req_data["toAddress"] = cleansed_dest_addr
        req_data["parcel"] = _MY_PARCEL
        req_data["rates"] = given_rates
        req_data["documents"] = [ _MY_SHIPMENT_DOCUMENT ]
        req_data["shipmentOptions"] = [
            { "name": "SHIPPER_ID", "value" : merchant_record["postalReportingNumber"] },
            { "name": "ADD_TO_MANIFEST", "value": "true" } 
        ]     
        result = call_shipping_api("/shipments", "POST", req_hdrs, req_params, req_data)
        shipmentId = result['data']["shipmentId"]
        print "shipment id is " + result["data"]["shipmentId"] 
        print "tracking id is " + result["data"]["parcelTrackingNumber"]
        print "label url is " + result["data"]["documents"][0]["contents"]
        
        # STEP 7: cancel the shipment for a refund
        req_hdrs = dict()
        req_hdrs["X-PB-TransactionId"] = getPbTxId()
        req_data = dict()
        req_data["carrier"] = "usps"
        api_path = "/shipments/" + urllib.quote_plus(utf8(shipmentId))
        result = call_shipping_api(api_path, "DELETE", req_hdrs, None, req_data)        
        print "cancel shipment request " + result['data']["status"]
        
    except urllib2.HTTPError, http_err:
        print "main - HTTP error: " + str(http_err.getcode()) + ": " + http_err.read()
    except Exception, e:
        print "main - exception: " + str(e)
        
    sys.exit(0)

if __name__ == '__main__':
    main()
