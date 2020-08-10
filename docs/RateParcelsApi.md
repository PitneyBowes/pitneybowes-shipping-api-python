# pbshipping.RateParcelsApi

All URIs are relative to *https://api-sandbox.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rate_parcel**](RateParcelsApi.md#rate_parcel) | **POST** /v1/rates | Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.


# **rate_parcel**
> Shipment rate_parcel(shipment, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_shipper_rate_plan=x_pb_shipper_rate_plan, x_pb_integrator_carrier_id=x_pb_integrator_carrier_id, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, include_delivery_commitment=include_delivery_commitment, carrier=carrier)

Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import pbshipping
from pbshipping.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pbshipping.Configuration(
    host = "https://api-sandbox.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = pbshipping.Configuration(
    host = "https://api-sandbox.pitneybowes.com/shippingservices"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pbshipping.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pbshipping.RateParcelsApi(api_client)
    shipment = {"fromAddress":{"company":"Supplier","name":"J. Smith","phone":"303-555-1213","email":"js@example.com","residential":false,"addressLines":["4750 Walnut Street"],"cityTown":"Boulder","stateProvince":"CO","postalCode":"80301","countryCode":"US"},"toAddress":{"company":"Shop","name":"J. Jones","phone":"203-000-1234","email":"jjones@example.com","residential":false,"addressLines":["771 Orange St"],"cityTown":"New Haven","stateProvince":"CT","postalCode":"06511","countryCode":"US"},"parcel":{"weight":{"weight":1,"unitOfMeasurement":"OZ"},"dimension":{"length":5,"width":0.25,"height":4,"unitOfMeasurement":"IN","irregularParcelGirth":1}},"rates":[{"carrier":"USPS","parcelType":"PKG","inductionPostalCode":"06484"}]} # Shipment | Shipment request for Rates
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
x_pb_shipper_rate_plan = 'x_pb_shipper_rate_plan_example' # str | USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq) (optional)
x_pb_integrator_carrier_id = 'x_pb_integrator_carrier_id_example' # str | USPS Only. Negotiated services rate, if applicable. (optional)
x_pb_shipper_carrier_account_id = 'x_pb_shipper_carrier_account_id_example' # str | UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API. (optional)
include_delivery_commitment = True # bool | When set to true, returns estimated transit time in days. (optional)
carrier = 'carrier_example' # str | Cross-Border only. Required for PB Cross-Border. Set this to PBI. (optional)

    try:
        # Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.
        api_response = api_instance.rate_parcel(shipment, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_shipper_rate_plan=x_pb_shipper_rate_plan, x_pb_integrator_carrier_id=x_pb_integrator_carrier_id, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, include_delivery_commitment=include_delivery_commitment, carrier=carrier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RateParcelsApi->rate_parcel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment** | [**Shipment**](Shipment.md)| Shipment request for Rates | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **x_pb_shipper_rate_plan** | **str**| USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq) | [optional] 
 **x_pb_integrator_carrier_id** | **str**| USPS Only. Negotiated services rate, if applicable. | [optional] 
 **x_pb_shipper_carrier_account_id** | **str**| UPS (United Parcel Service) Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account](https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) API. | [optional] 
 **include_delivery_commitment** | **bool**| When set to true, returns estimated transit time in days. | [optional] 
 **carrier** | **str**| Cross-Border only. Required for PB Cross-Border. Set this to PBI. | [optional] 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

