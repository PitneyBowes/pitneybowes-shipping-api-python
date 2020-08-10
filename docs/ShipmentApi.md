# pbshipping.ShipmentApi

All URIs are relative to *https://api-sandbox.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_shipment**](ShipmentApi.md#cancel_shipment) | **DELETE** /v1/shipments/{shipmentId} | cancelShipment
[**create_shipment_label**](ShipmentApi.md#create_shipment_label) | **POST** /v1/shipments | This operation creates a shipment and purchases a shipment label.
[**reprint_shipment**](ShipmentApi.md#reprint_shipment) | **GET** /v1/shipments/{shipmentId} | reprintShipment
[**retry_shipment**](ShipmentApi.md#retry_shipment) | **GET** /v1/shipments | retryShipment


# **cancel_shipment**
> CancelShipment cancel_shipment(x_pb_transaction_id, shipment_id, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, cancel_initiator=cancel_initiator, carrier=carrier)

cancelShipment

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
    api_instance = pbshipping.ShipmentApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
shipment_id = 'shipment_id_example' # str | shipmentId
x_pb_unified_error_structure = 'true' # str | Recommended. Set this to true to use the standard error object if an error occurs. (optional) (default to 'true')
x_pb_shipper_carrier_account_id = 'x_pb_shipper_carrier_account_id_example' # str | UPS Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account API.(https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) (optional)
cancel_initiator = 'SHIPPER' # str | Indicates that this refund request is initiated by the shipper. Set this to: SHIPPER (optional)
carrier = pbshipping.Carrier() # Carrier | Conditional. The carrier. This is required if the carrier is not USPS (optional)

    try:
        # cancelShipment
        api_response = api_instance.cancel_shipment(x_pb_transaction_id, shipment_id, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, cancel_initiator=cancel_initiator, carrier=carrier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipmentApi->cancel_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **shipment_id** | **str**| shipmentId | 
 **x_pb_unified_error_structure** | **str**| Recommended. Set this to true to use the standard error object if an error occurs. | [optional] [default to &#39;true&#39;]
 **x_pb_shipper_carrier_account_id** | **str**| UPS Only. The unique identifier returned in the shipperCarrierAccountId field by the [Register an Existing Carrier Account API.(https://shipping.pitneybowes.com/api/post-carrier-accounts-register.html) | [optional] 
 **cancel_initiator** | **str**| Indicates that this refund request is initiated by the shipper. Set this to: SHIPPER | [optional] 
 **carrier** | [**Carrier**](.md)| Conditional. The carrier. This is required if the carrier is not USPS | [optional] 

### Return type

[**CancelShipment**](CancelShipment.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shipment_label**
> Shipment create_shipment_label(x_pb_transaction_id, shipment, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_integrator_carrier_id=x_pb_integrator_carrier_id, x_pb_shipper_rate_plan=x_pb_shipper_rate_plan, x_pb_shipment_group_id=x_pb_shipment_group_id, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, include_delivery_commitment=include_delivery_commitment)

This operation creates a shipment and purchases a shipment label.

The API returns the label as either a Base64 string or a link to a PDF. For more information visit [Create Shipment Documents](https://shipping.pitneybowes.com/api/post-shipments.html). Following are samples of different carriers -  * [Create a USPS (U.S. Postal Service) Label](https://shipping.pitneybowes.com/api/post-shipments-usps.html)  * [Create a USPS PMOD Label](https://shipping.pitneybowes.com/api/post-shipments-pmod.html) * [Create a USPS Scan-Based Return Label](https://shipping.pitneybowes.com/api/post-shipments-returns.html) * [Create a Pure Post Return Label](https://shipping.pitneybowes.com/api/post-shipments-pure-post-return.html) * [Create a Newgistics Label](https://shipping.pitneybowes.com/api/post-shipments-newgistics.html) * [Create a PB Presort Label](https://shipping.pitneybowes.com/api/post-shipments-presort.html) * [Create a PB Cross-Border Shipment](https://shipping.pitneybowes.com/api/post-shipments-cbds.html) * [Create a UPS (United Parcel Service) Label](https://shipping.pitneybowes.com/api/post-shipments-ups.html)

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
    api_instance = pbshipping.ShipmentApi(api_client)
    x_pb_transaction_id = 'uniquevalue' # str | Required. A unique identifier for the transaction, up to 25 characters.
shipment = {"fromAddress":{"company":"Pitney Bowes Inc.","name":"Paul Wright","phone":"203-555-1430","email":"john.publica@pb.com","residential":false,"addressLines":["27 Waterview Drive"],"cityTown":"Shelton","stateProvince":"CT","postalCode":"06484","countryCode":"US"},"toAddress":{"company":"ABC Company","name":"Rufous Sirius Canid","phone":"323 555-1212","email":"rs.canid@gmail.com","residential":true,"addressLines":["631 S Main St"],"cityTown":"Greenville","stateProvince":"SC","postalCode":"29601","countryCode":"US"},"parcel":{"weight":{"unitOfMeasurement":"OZ","weight":38},"dimension":{"unitOfMeasurement":"IN","length":6,"width":6,"height":6}},"rates":[{"carrier":"USPS","serviceId":"PM","parcelType":"PKG","specialServices":[{"specialServiceId":"DelCon","inputParameters":[{"name":"INPUT_VALUE","value":"0"}]}],"inductionPostalCode":"06484"}],"documents":[{"type":"SHIPPING_LABEL","contentType":"URL","size":"DOC_4X6","fileFormat":"PDF","printDialogOption":"NO_PRINT_DIALOG"}],"shipmentOptions":[{"name":"SHIPPER_ID","value":"3000090171"},{"name":"ADD_TO_MANIFEST","value":"true"},{"name":"HIDE_TOTAL_CARRIER_CHARGE","value":"true"},{"name":"PRINT_CUSTOM_MESSAGE_1","value":"custom message for label"},{"name":"SHIPPING_LABEL_RECEIPT","value":"NO_OPTIONS"}]} # Shipment | request
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
x_pb_integrator_carrier_id = 'x_pb_integrator_carrier_id_example' # str | USPS Only. Negotiated services rate, if applicable. (optional)
x_pb_shipper_rate_plan = 'x_pb_shipper_rate_plan_example' # str | USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq). (optional)
x_pb_shipment_group_id = 'x_pb_shipment_group_id_example' # str |  **[Required parameter for PBPresort service](https://shipping.pitneybowes.com/api/post-shipments-presort.html)**.The job number that represents the agreement between the merchant and PB Presort. This was provided by Pitney Bowes during [merchant onboarding for PB Presort](https://shipping.pitneybowes.com/carriers/pb-presort.html). (optional)
x_pb_shipper_carrier_account_id = 'x_pb_shipper_carrier_account_id_example' # str | **[Required parameter for PBPresort service](https://shipping.pitneybowes.com/api/post-shipments-presort.html)**. The merchant's Mailer ID (MID), as provided by Pitney Bowes during merchant onboarding for PB Presort. (optional)
include_delivery_commitment = 'include_delivery_commitment_example' # str | If set to true, returns estimated transit times in days. Only for USPS Create Shipment. See also [Pitney Bowes Delivery Guarantee](https://shipping.pitneybowes.com/faqs/delivery-guarantee.html) [Do all USPS services return transit times?](https://shipping.pitneybowes.com/faqs/shipments.html#transit-times-faq) (optional)

    try:
        # This operation creates a shipment and purchases a shipment label.
        api_response = api_instance.create_shipment_label(x_pb_transaction_id, shipment, x_pb_unified_error_structure=x_pb_unified_error_structure, x_pb_integrator_carrier_id=x_pb_integrator_carrier_id, x_pb_shipper_rate_plan=x_pb_shipper_rate_plan, x_pb_shipment_group_id=x_pb_shipment_group_id, x_pb_shipper_carrier_account_id=x_pb_shipper_carrier_account_id, include_delivery_commitment=include_delivery_commitment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipmentApi->create_shipment_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **shipment** | [**Shipment**](Shipment.md)| request | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **x_pb_integrator_carrier_id** | **str**| USPS Only. Negotiated services rate, if applicable. | [optional] 
 **x_pb_shipper_rate_plan** | **str**| USPS Only. Shipper rate plan, if applicable. For more information, see [this FAQ](https://shipping.pitneybowes.com/faqs/rates.html#rate-plans-faq). | [optional] 
 **x_pb_shipment_group_id** | **str**|  **[Required parameter for PBPresort service](https://shipping.pitneybowes.com/api/post-shipments-presort.html)**.The job number that represents the agreement between the merchant and PB Presort. This was provided by Pitney Bowes during [merchant onboarding for PB Presort](https://shipping.pitneybowes.com/carriers/pb-presort.html). | [optional] 
 **x_pb_shipper_carrier_account_id** | **str**| **[Required parameter for PBPresort service](https://shipping.pitneybowes.com/api/post-shipments-presort.html)**. The merchant&#39;s Mailer ID (MID), as provided by Pitney Bowes during merchant onboarding for PB Presort. | [optional] 
 **include_delivery_commitment** | **str**| If set to true, returns estimated transit times in days. Only for USPS Create Shipment. See also [Pitney Bowes Delivery Guarantee](https://shipping.pitneybowes.com/faqs/delivery-guarantee.html) [Do all USPS services return transit times?](https://shipping.pitneybowes.com/faqs/shipments.html#transit-times-faq) | [optional] 

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
**201** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reprint_shipment**
> Shipment reprint_shipment(shipment_id, x_pb_unified_error_structure=x_pb_unified_error_structure, carrier=carrier)

reprintShipment

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
    api_instance = pbshipping.ShipmentApi(api_client)
    shipment_id = 'shipment_id_example' # str | Required. The shipment ID that was issued when shipment label was generated.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
carrier = pbshipping.Carrier() # Carrier |  (optional)

    try:
        # reprintShipment
        api_response = api_instance.reprint_shipment(shipment_id, x_pb_unified_error_structure=x_pb_unified_error_structure, carrier=carrier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipmentApi->reprint_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| Required. The shipment ID that was issued when shipment label was generated. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **carrier** | [**Carrier**](.md)|  | [optional] 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_shipment**
> Shipment retry_shipment(original_transaction_id, x_pb_unified_error_structure=x_pb_unified_error_structure, carrier=carrier)

retryShipment

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
    api_instance = pbshipping.ShipmentApi(api_client)
    original_transaction_id = '12344' # str | 
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
carrier = pbshipping.Carrier() # Carrier |  (optional)

    try:
        # retryShipment
        api_response = api_instance.retry_shipment(original_transaction_id, x_pb_unified_error_structure=x_pb_unified_error_structure, carrier=carrier)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ShipmentApi->retry_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_transaction_id** | **str**|  | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **carrier** | [**Carrier**](.md)|  | [optional] 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

