# pbshipping.TrackingApi

All URIs are relative to *https://api-sandbox.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tracking_events**](TrackingApi.md#add_tracking_events) | **POST** /v2/track/events | getTrackingDetails
[**get_tracking_details**](TrackingApi.md#get_tracking_details) | **GET** /v1/tracking/{trackingNumber} | getTrackingDetails


# **add_tracking_events**
> InlineResponse2002 add_tracking_events(add_tracking_events, x_pb_unified_error_structure=x_pb_unified_error_structure)

getTrackingDetails

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
    api_instance = pbshipping.TrackingApi(api_client)
    add_tracking_events = {"carrier":"NEWGISTICS","references":[{"referenceType":"package","referenceValue":"1Z00","events":[{"eventCode":"DPB","carrierEventCode":"DOAC","eventDate":"2020-04-18","eventTime":"12:48:10","eventTimeOffset":"-06:00","eventCity":"Decatur","eventStateOrProvince":"IL","postalCode":"62521","country":"US"}]},{"referenceType":"package","referenceValue":"3Z30","events":[{"eventCode":"DPB","carrierEventCode":"DOAC","eventDate":"2020-04-18","eventTime":"12:50:00","eventTimeOffset":"-06:00","eventCity":"Decatur","eventStateOrProvince":"IL","postalCode":"62521","country":"US"}]}]} # AddTrackingEvents | add track event
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # getTrackingDetails
        api_response = api_instance.add_tracking_events(add_tracking_events, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrackingApi->add_tracking_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_tracking_events** | [**AddTrackingEvents**](AddTrackingEvents.md)| add track event | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Error |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_details**
> TrackingResponse get_tracking_details(tracking_number, package_identifier_type, carrier, x_pb_unified_error_structure=x_pb_unified_error_structure)

getTrackingDetails

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
    api_instance = pbshipping.TrackingApi(api_client)
    tracking_number = 'tracking_number_example' # str | The tracking number for the shipment.
package_identifier_type = 'TrackingNumber' # str | packageIdentifierType (default to 'TrackingNumber')
carrier = 'carrier_example' # str | carrier
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # getTrackingDetails
        api_response = api_instance.get_tracking_details(tracking_number, package_identifier_type, carrier, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrackingApi->get_tracking_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_number** | **str**| The tracking number for the shipment. | 
 **package_identifier_type** | **str**| packageIdentifierType | [default to &#39;TrackingNumber&#39;]
 **carrier** | **str**| carrier | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**TrackingResponse**](TrackingResponse.md)

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

