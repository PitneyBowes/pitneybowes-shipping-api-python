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
# File: shipping_resource.py
# Description: shipping API resource classes (e.g.: shipment, manifest)
#

from __builtin__ import classmethod

from pbshipping import error
from pbshipping import Configuration
from pbshipping.resource import APIObject, APIResource

def get_api_version(api_key):
    if api_key in Configuration.params["override_api_version"]:
        return Configuration.params["override_api_version"][api_key]
    else:
        return Configuration.params["default_api_version"]

class ShippingAPIResource(APIResource):
    
    def request(self, auth_obj, method, api_version, api_path, headers, params, 
                post_data):
        return super(ShippingAPIResource, self).request(auth_obj, method, 
                    Configuration.api_group_shipping, api_version, api_path, headers, 
                     params, post_data)
                
class Account(ShippingAPIResource):

    #
    # MANAGING MERCHANTS
    # API: GET /ledger/accounts/{accountNumber}/balance
    # API signature: get/ledger/accounts/.../balance
    #
    # Retrieve the account balance of a merchant account.   
    #
    def getBalance(self, auth_obj):
        if self.accountNumber is None:
            raise error.MissingResourceAttribute("accountNumber")
        api_path = "/ledger/accounts/" + self.accountNumber + "/balance"
        api_version = get_api_version("get/ledger/accounts/.../balance")
        json_resp = super(Account, self).request("get", auth_obj, api_version, 
            api_path, None, None, None)
        return APIObject(json_resp)
 
    @classmethod
    def getBalanceByAccountNumber(cls, auth_obj, thisAcccountNumber):
        instance = Account(accountNumber=thisAcccountNumber)
        return instance.getBalance(auth_obj)        

class Address(ShippingAPIResource):

    #
    # ADDRESS VALIDATION
    # API: POST /addresses/verify
    # API signature: post/addresses/verify
    #
    # Verify and cleanse any postal address within the United States. 
    # This will ensure that packages are rated accurately and the 
    # shipments arrive at their final destination on time.
    # 
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead. 
    #
    def verify(self, auth_obj, minimalAddressValidation=None, overwrite=True):
        if minimalAddressValidation is None:
            hdrs = {"minimalAddressValidation": False}            
        else:
            hdrs = {"minimalAddressValidation": minimalAddressValidation}
        api_version = get_api_version("post/addresses/verify")
        json_resp = super(Address, self).request("post", auth_obj, 
            api_version, "/addresses/verify", hdrs, None, self)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Address(json_resp)

class Carrier(ShippingAPIResource):

    #
    # COUNTRIES LIST
    # API: GET /countries
    # API signature: get/countries
    #
    # Returns a list of supported destination countries to which the carrier 
    # offers international shipping services. 
    #
    def getCountries(self, auth_obj, originCountryCode):
        if self.name is None:
            raise error.MissingResourceAttribute("name")
        params = {"carrier": self.name, "originCountryCode": originCountryCode}
        api_version = get_api_version("get/countries")
        json_resp = super(Carrier, self).request("get", auth_obj, api_version, 
            "/countries", None, params, None)
        return [Country(nextobj) for nextobj in json_resp] 
        
    @classmethod
    def getCountriesForCarrier(cls, auth_obj, carrier, originCountryCode):
        instance = Carrier(name=carrier)
        return instance.getCountries(auth_obj, originCountryCode)

class Country(ShippingAPIResource):
    pass
    
class Customs(ShippingAPIResource):
    pass

class CustomsInfo(ShippingAPIResource):
    pass
    
class CustomsItem(ShippingAPIResource):
    pass
        
class Discount(ShippingAPIResource):
    pass
                        
class Document(ShippingAPIResource):
    pass
        
class DeliveryCommitment(ShippingAPIResource):
    pass
    
class Developer(ShippingAPIResource):

    #
    # MANAGING MERCHANTS
    # API: GET /developers/{developerId}/merchants/emails/{emailId}/
    # API signature: get/developers/.../merchants/emails/...
    #
    # Register your merchants or shippers, if you have signed up for the 
    # individual account payment model.
    #
    # This method allows you to retrieve the merchant ID and related
    # information based on the Email ID they used while registering, 
    # so that you can request transactions on their behalf.  
    #       
    def registerMerchantIndividualAccount(self, auth_obj, emailid):
        if self.developerid is None:
            raise error.MissingResourceAttribute("developerid")
        api_path = "/developers/" + self.developerid 
        api_path += "/merchants/emails/" + emailid + "/"
        api_version = get_api_version("get/developers/.../merchants/emails/...")
        json_resp = super(Developer, self).request("get", auth_obj, api_version, 
            api_path, None, None, None) 
        return Merchant(json_resp)
 
    #
    # MANAGING MERCHANTS
    # API: POST /developers/{developerId}/merchants/registration
    # API signature: post/developers/.../merchants/registration
    #   
    # Register your merchants or shippers, if you have signed up for the 
    # bulk account payment model.
    # 
    # This method allows you to retrieve the merchant ID and related
    # information, so that you can request transactions on their behalf. 
    #
    def registerMerchantBulkAccount(self, auth_obj, address):
        if self.developerid is None:
            raise error.MissingResourceAttribute("developerid")
        api_path = "/developers/" + self.developerid
        api_path += "/merchants/registration"
        api_version = get_api_version("post/developers/.../merchants/registration")
        json_resp = super(Developer, self).request("post", auth_obj, api_version, 
            api_path, None, None, address)
        return Merchant(json_resp)

    #
    # MANAGING MERCHANTS
    # API: GET /ledger/developers/{developerId}/transactions/reports
    # API signature: get/ledger/developers/.../transactions/reports
    #
    # Retrieve all transactions based on the given input parameters   
    #    
    def getTransactionReport(self, auth_obj, params):
        if self.developerid is None:
            raise error.MissingResourceAttribute("developerid")
        api_path = "/ledger/developers/" + self.developerid 
        api_path += "/transactions/reports"
        api_version = get_api_version("get/ledger/developers/.../transactions/reports")
        json_resp = super(Developer, self).request("get", auth_obj, api_version, 
            api_path, None, params, None)
        return APIObject(json_resp)
           
class Manifest(ShippingAPIResource):
    
    # 
    # MANAGING MANIFESTS
    # API: POST /manifests
    # API signature: post/manifests
    #
    # Create a USPS scan form
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead
    #
    def create(self, auth_obj, txid, overwrite=True):
        if self.carrier is None:
            raise error.MissingResourceAttribute("carrier")
        elif self.parcelTrackingNumbers is None:
            raise error.MissingResourceAttribute("parcelTrackingNumbers")
        elif self.submissionDate is None:
            raise error.MissingResourceAttribute("submissionDate")            
        elif self.fromAddress is None:
            raise error.MissingResourceAttribute("fromAddress")
        hdrs = {Configuration.txid_attrname: txid}
        post_data = {"carrier": self.carrier,
                     "parcelTrackingNumbers": self.parcelTrackingNumbers,
                     "submissionDate": self.submissionDate,
                     "fromAddress": self.fromAddress}
        api_version = get_api_version("post/manifests")
        json_resp = super(Manifest, self).request("post", auth_obj, api_version, 
            "/manifests", hdrs, None, post_data)
        if overwrite == True:
            self.update(json_resp) 
            return self       
        else:
            return Manifest(json_resp)

    # 
    # MANAGING MANIFESTS
    # API: GET /manifests/{manifestId}
    # API signature: get/manifests/...
    #
    # Reprint the USPS scan form
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead    
    #
    def reprint(self, auth_obj, overwrite=True):
        if self.manifestId is None:
            raise error.MissingResourceAttribute("manifestId")
        api_path = "/manifests/" + self.manifestId
        api_version = get_api_version("get/manifests/...")
        json_resp = super(Manifest, self).request("get", auth_obj, api_version, 
            api_path, None, None, None)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Manifest(json_resp)
        
    @classmethod
    def reprintById(cls, auth_obj, thisManifestId):
        return Manifest(manifestId=thisManifestId).reprint(auth_obj)

    # 
    # MANAGING MANIFESTS
    # API: GET /manifests
    # API signature: get/manifests/
    #
    # Retry a manifest request that was previously submitted with no successful 
    # response
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead      
    #
    def retry(self, auth_obj, txid, thisOriginalTransactionId, overwrite=True):
        hdrs = {Configuration.txid_attrname: txid}
        params = {"originalTransactionId": thisOriginalTransactionId}
        api_version = get_api_version("get/manifests")
        json_resp = self.request("get", auth_obj, api_version, "/manifests", 
            hdrs, params, None)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Manifest(json_resp)
                    
    @classmethod
    def retryByTransactionId(cls, auth_obj, txid, thisOriginalTransactionId):
        return Manifest().retry(auth_obj, txid, thisOriginalTransactionId)
    
class Merchant(ShippingAPIResource):
    pass

class Parameter(ShippingAPIResource):
    pass

class Parcel(ShippingAPIResource):
    pass

class ParcelDimension(ShippingAPIResource):
    pass    
     
class ParcelWeight(ShippingAPIResource):
    pass
            
class Rate(ShippingAPIResource):
    pass

class ScanDetails(ShippingAPIResource):
    pass
                  
class Shipment(ShippingAPIResource):

    # 
    # MANAGING RATES AND SHIPMENTS
    # API: POST /rates
    # API signature: post/rates
    #
    # Rate a shipment before a shipment label is purchased and printed.
    #    
    def getRates(self, auth_obj, txid, includeDeliveryCommitment=None,
                 extraHdrs=None):
        hdrs = {Configuration.txid_attrname: txid}
        if extraHdrs is not None:
            hdrs.update(extraHdrs)
        if includeDeliveryCommitment is None:
            params = {"includeDeliveryCommitment": False}            
        else:
            params = {"includeDeliveryCommitment": includeDeliveryCommitment}
        api_version = get_api_version("post/rates")
        json_resp = super(Shipment, self).request("post", auth_obj, api_version,
            "/rates", hdrs, params, self)
        return [Rate(nextobj) for nextobj in json_resp["rates"]] 

    # 
    # MANAGING RATES AND SHIPMENTS
    # API: POST /shipments/
    # API signature: post/shipments
    #
    # Create a shipment and purchase a shipment label.
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead
    # 
    def createAndPurchase(self, auth_obj, txid, includeDeliveryCommitment=None,
                          extraHdrs=None, overwrite=True):
        hdrs = {Configuration.txid_attrname: txid}
        if extraHdrs is not None:
            hdrs.update(extraHdrs)
        if includeDeliveryCommitment is None:
            params = {"includeDeliveryCommitment": False}            
        else:
            params = {"includeDeliveryCommitment": includeDeliveryCommitment}
        api_version = get_api_version("post/shipments")
        json_resp = super(Shipment, self).request("post", auth_obj, api_version, 
            "/shipments", hdrs, params, 
            self)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Shipment(json_resp)

    # 
    # MANAGING RATES AND SHIPMENTS
    # API: GET /shipments/{shipmentId}
    # API signature: get/shipments/...
    #
    # Reprint a shipment label. 
    # Note that the number of reprints of a shipment label will be scrutinized 
    # and restricted.
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead      
    # 
    def reprintLabel(self, auth_obj, overwrite=True):
        if self.shipmentId is None:
            raise error.MissingResourceAttribute("shipmentId")
        api_version = get_api_version("get/shipments/...")
        json_resp = super(Shipment, self).request("get", auth_obj, api_version,
            "/shipments/" + self.shipmentId , 
            None, None, None)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Shipment(json_resp)
        
    @classmethod
    def reprintLabelByShipmentId(cls, auth_obj, thisShipmentId):
        return Shipment(shipmentId=thisShipmentId).reprintLabel(auth_obj)
  
    # 
    # MANAGING RATES AND SHIPMENTS
    # API: GET /shipments?originalTransactionId
    # API signature: get/shipments
    #
    # Retry a shipment that was previously submitted with no successful response.
    #
    # By default, the returned result would overwrite the current state 
    # of the object. To avoid overwriting, set the input argument 
    # overwrite to False and a copy of the result would be generated and
    # returned instead  
    #          
    def retry(self, auth_obj, txid, originalTxId, overwrite=True):
        hdrs = {Configuration.txid_attrname: txid}
        params = {"originalTransactionId": originalTxId}
        api_version = get_api_version("get/shipments")
        json_resp = super(Shipment, self).request("get", auth_obj, api_version,
            "/shipments", hdrs, params, None)
        if overwrite == True:
            self.update(json_resp)
            return self
        else:
            return Shipment(json_resp)

    @classmethod
    def retryByTransactionId(cls, auth_obj, txid, originalTxId):
        return Shipment().retry(auth_obj, txid, originalTxId)

    # 
    # MANAGING RATES AND SHIPMENTS
    # API: DELETE /shipment/{shipmentId}
    # API signature: delete/shipments/...
    #
    # Cancel/void a shipment, and submit the shipment label for refund.
    #     
    def cancel(self, auth_obj, txid, carrier, cancelInitiator=None):
        if self.shipmentId is None:
            raise error.MissingResourceAttribute("shipmentId")
        hdrs = {Configuration.txid_attrname: txid}
        data = dict()
        data["carrier"] = carrier
        if cancelInitiator != None:
            data["cancelInitiator"] = cancelInitiator
        api_version = get_api_version("delete/shipments/...")
        json_resp = super(Shipment, self).request("delete", auth_obj, api_version,
            "/shipments/" + self.shipmentId, 
            hdrs, None, data)
        return APIObject(json_resp)
    
    @classmethod
    def cancelByShipmentId(cls, auth_obj, txid, thisShipmentId, carrier, 
                           cancelInitiator=None):
        shipmentObj = Shipment(shipmentId=thisShipmentId) 
        if cancelInitiator is None:
            return shipmentObj.cancel(auth_obj, txid, carrier)
        else:
            return shipmentObj.cancel(auth_obj, txid, carrier, cancelInitiator)

class ShipmentOptions(ShippingAPIResource):
    pass
    
class ShippingLabel(ShippingAPIResource):
    pass

class SpecialService(ShippingAPIResource):
    pass

class Surcharge(ShippingAPIResource):
    pass
    
class Tax(ShippingAPIResource):
    pass
            
class Tracking(ShippingAPIResource):
    
    #
    # TRACKING
    # API: GET /tracking/{trackingNumber}
    # API signature: get/tracking/...
    #
    # Shipment labels that are printed using the Pitney Bowes APIs are 
    # automatically tracked and their package status can be easily retrieved 
    # using this implementation of the GET operation.
    #
    def updateStatus(self, auth_obj):
        if self.trackingNumber is None:
            raise error.MissingResourceAttribute("trackingNumber")    
        if self.packageIdentiferType is None:
            self.packageIdentiferType = "TrackingNumber"
        if self.carrier is None:
            self.carrier = "USPS"
        params = {"carrier": self.carrier, 
                  "packageIdentifierType": self.packageIdentiferType}
        api_path = "/tracking/" + self.trackingNumber
        api_version = get_api_version("get/tracking/...")
        json_resp = super(Tracking, self).request("get", auth_obj, api_version,
            api_path, None, params, None)        
        self.update(json_resp)    

        
class TransactionDetails(ShippingAPIResource):
    pass
