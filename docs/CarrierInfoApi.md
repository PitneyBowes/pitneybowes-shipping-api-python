# pitneybowes_shippingapi.CarrierInfoApi

All URIs are relative to *https://api-qa.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_carrier_facilities**](CarrierInfoApi.md#get_carrier_facilities) | **POST** /v1/carrier-facility | Find Carrier Facilities
[**get_carrier_license_agreement**](CarrierInfoApi.md#get_carrier_license_agreement) | **GET** /v1/carrier/license-agreements | This operation retrieves a carrier&#39;s license agreement.
[**get_carrier_service_rules**](CarrierInfoApi.md#get_carrier_service_rules) | **GET** /v1/information/rules/rating-services | Retrieves the rules governing the carrier&#39;s services.
[**get_carrier_supported_destination**](CarrierInfoApi.md#get_carrier_supported_destination) | **GET** /v1/countries | This operation returns a list of supported destination countries to which the carrier offers international shipping services.


# **get_carrier_facilities**
> CarrierFacilityResponse get_carrier_facilities(carrier_facility_request, x_pb_unified_error_structure=x_pb_unified_error_structure)

Find Carrier Facilities

This operation locates Post Offices and other facilities for a given carrier. You can use this operation, for example, to locate all USPS Post Offices near to a given postal code.If you use the Standard Return API and if you use the option to print a QR code, use this API to locate facilities where the buyer can print the label from the QR code.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import pitneybowes_shippingapi
from pitneybowes_shippingapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-qa.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pitneybowes_shippingapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pitneybowes_shippingapi.CarrierInfoApi(api_client)
    carrier_facility_request = {"address":{"addressLines":["6525 Greenway Dr"],"cityTown":"Roanoke","stateProvince":"VA","countryCode":"US"},"carrier":"USPS","carrierFacilityOptions":[{"name":"FACILITY_TYPE_SERVICE","value":"LABEL_BROKER_RETAIL"},{"name":"FACILITY_TYPE","value":"POST_OFFICE"},{"name":"FACILITY_WITHIN_RADIUS","value":"10"},{"name":"NUMBER_OF_FACILITIES","value":"5"}]} # CarrierFacilityRequest | 
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Find Carrier Facilities
        api_response = api_instance.get_carrier_facilities(carrier_facility_request, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CarrierInfoApi->get_carrier_facilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_facility_request** | [**CarrierFacilityRequest**](CarrierFacilityRequest.md)|  | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**CarrierFacilityResponse**](CarrierFacilityResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carrier_license_agreement**
> InlineResponse200 get_carrier_license_agreement(carrier, origin_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure)

This operation retrieves a carrier's license agreement.

This operation retrieves a carrier's license agreement. The operation is used in the [Carrier Registration Tutorial](https://shipping.pitneybowes.com/carrier-registration.html).

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import pitneybowes_shippingapi
from pitneybowes_shippingapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-qa.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pitneybowes_shippingapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pitneybowes_shippingapi.CarrierInfoApi(api_client)
    carrier = 'UPS' # str | The carrier name. Currently this must be set to: UPS (default to 'UPS')
origin_country_code = pitneybowes_shippingapi.ISOCountryCode() # ISOCountryCode | The two-character ISO country code for the country where the shipment originates.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # This operation retrieves a carrier's license agreement.
        api_response = api_instance.get_carrier_license_agreement(carrier, origin_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CarrierInfoApi->get_carrier_license_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier** | **str**| The carrier name. Currently this must be set to: UPS | [default to &#39;UPS&#39;]
 **origin_country_code** | [**ISOCountryCode**](.md)| The two-character ISO country code for the country where the shipment originates. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carrier_service_rules**
> CarrierRule get_carrier_service_rules(carrier, origin_country_code, destination_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure, rate_type_id=rate_type_id, future_shipment_date=future_shipment_date, return_shipment=return_shipment, compact_response=compact_response)

Retrieves the rules governing the carrier's services.

This operation retrieves the rules governing the carrier's services, including the available parcel types and the limits on weights and dimensions. **This API currently returns rules only for USPS** . Find more information at [Get Carrier Rules](https://shipping.pitneybowes.com/api/get-carrier-rules.html)

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import pitneybowes_shippingapi
from pitneybowes_shippingapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-qa.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pitneybowes_shippingapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pitneybowes_shippingapi.CarrierInfoApi(api_client)
    carrier = pitneybowes_shippingapi.Carrier() # Carrier | The carrier name. **Currently this must be set to: USPS** 
origin_country_code = pitneybowes_shippingapi.ISOCountryCode() # ISOCountryCode | The [two-character ISO country code](https://www.iso.org/obp/ui/#search) for the country where the shipment originates.
destination_country_code = pitneybowes_shippingapi.ISOCountryCode() # ISOCountryCode | The [two-character ISO country code](https://www.iso.org/obp/ui/#search) for the country of the shipment's destination address.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
rate_type_id = 'rate_type_id_example' # str | The type of rate requested, such as COMMERCIAL_BASE. If a rate type is not specified, all eligible rate types are returned. (optional)
future_shipment_date = 'future_shipment_date_example' # str | If the shipment is for a future date, and if a rate change is expected before the shipment date, use this field to ensure you get the correct rates and correct rate rules. Note that a rate change can affect the structure of the rate rules as well as the actual rates.Specify this value in UTC/GMT, not in local time. Formats allowed are   * **YYYY-MM-DD**   * **YYYY-MM-DD HH:mm:ss** * **YYYY-MM-DD HH:mm:ss.SSS** (optional)
return_shipment = '2013-10-20T19:20:30+01:00' # datetime | If set to true, provides only services applicable for return shipment. (optional)
compact_response = True # bool | If set to true, returns only summary, without special service details. (optional)

    try:
        # Retrieves the rules governing the carrier's services.
        api_response = api_instance.get_carrier_service_rules(carrier, origin_country_code, destination_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure, rate_type_id=rate_type_id, future_shipment_date=future_shipment_date, return_shipment=return_shipment, compact_response=compact_response)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CarrierInfoApi->get_carrier_service_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier** | [**Carrier**](.md)| The carrier name. **Currently this must be set to: USPS**  | 
 **origin_country_code** | [**ISOCountryCode**](.md)| The [two-character ISO country code](https://www.iso.org/obp/ui/#search) for the country where the shipment originates. | 
 **destination_country_code** | [**ISOCountryCode**](.md)| The [two-character ISO country code](https://www.iso.org/obp/ui/#search) for the country of the shipment&#39;s destination address. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **rate_type_id** | **str**| The type of rate requested, such as COMMERCIAL_BASE. If a rate type is not specified, all eligible rate types are returned. | [optional] 
 **future_shipment_date** | **str**| If the shipment is for a future date, and if a rate change is expected before the shipment date, use this field to ensure you get the correct rates and correct rate rules. Note that a rate change can affect the structure of the rate rules as well as the actual rates.Specify this value in UTC/GMT, not in local time. Formats allowed are   * **YYYY-MM-DD**   * **YYYY-MM-DD HH:mm:ss** * **YYYY-MM-DD HH:mm:ss.SSS** | [optional] 
 **return_shipment** | **datetime**| If set to true, provides only services applicable for return shipment. | [optional] 
 **compact_response** | **bool**| If set to true, returns only summary, without special service details. | [optional] 

### Return type

[**CarrierRule**](CarrierRule.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | For a list of all PB Shipping APIs error codes, please see [Error Codes](https://shipping.pitneybowes.com/reference/error-codes.html) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carrier_supported_destination**
> list[object] get_carrier_supported_destination(carrier, origin_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure)

This operation returns a list of supported destination countries to which the carrier offers international shipping services.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import pitneybowes_shippingapi
from pitneybowes_shippingapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api-qa.pitneybowes.com/shippingservices
# See configuration.py for a list of all supported configuration parameters.
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2ClientCredentials
configuration = pitneybowes_shippingapi.Configuration(
    host = "https://api-qa.pitneybowes.com/shippingservices"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pitneybowes_shippingapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pitneybowes_shippingapi.CarrierInfoApi(api_client)
    carrier = pitneybowes_shippingapi.Carrier() # Carrier | The carrier name. Currently this must be set to: USPS
origin_country_code = pitneybowes_shippingapi.ISOCountryCode() # ISOCountryCode | The two-character ISO country code for the country where the shipment originates.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # This operation returns a list of supported destination countries to which the carrier offers international shipping services.
        api_response = api_instance.get_carrier_supported_destination(carrier, origin_country_code, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CarrierInfoApi->get_carrier_supported_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier** | [**Carrier**](.md)| The carrier name. Currently this must be set to: USPS | 
 **origin_country_code** | [**ISOCountryCode**](.md)| The two-character ISO country code for the country where the shipment originates. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

**list[object]**

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

