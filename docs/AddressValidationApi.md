# pitneybowes_shippingapi.AddressValidationApi

All URIs are relative to *https://api-qa.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_address**](AddressValidationApi.md#verify_address) | **POST** /v1/addresses/verify | Address validation
[**verify_and_suggest_address**](AddressValidationApi.md#verify_and_suggest_address) | **POST** /v1/addresses/verify-suggest | Address Suggestion


# **verify_address**
> Address verify_address(address, x_pb_unified_error_structure=x_pb_unified_error_structure, minimal_address_validation=minimal_address_validation)

Address validation

Address validation verifies and cleanses postal addresses within the United States to help ensure packages are rated accurately and shipments arrive at their final destinations on time.

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
    api_instance = pitneybowes_shippingapi.AddressValidationApi(api_client)
    address = pitneybowes_shippingapi.Address() # Address | Address object that needs to be validated.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
minimal_address_validation = True # bool | When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check. (optional)

    try:
        # Address validation
        api_response = api_instance.verify_address(address, x_pb_unified_error_structure=x_pb_unified_error_structure, minimal_address_validation=minimal_address_validation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressValidationApi->verify_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](Address.md)| Address object that needs to be validated. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **minimal_address_validation** | **bool**| When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check. | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_and_suggest_address**
> AddressSuggestionResponse verify_and_suggest_address(return_suggestions, address, x_pb_unified_error_structure=x_pb_unified_error_structure)

Address Suggestion

This operation returns suggested addresses. Use this if the [Address Validation API](https://shipping.pitneybowes.com/api/post-address-verify.html) call has returned an error.

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
    api_instance = pitneybowes_shippingapi.AddressValidationApi(api_client)
    return_suggestions = 'true' # str | To return suggested addresses, set this to true. (default to 'true')
address = pitneybowes_shippingapi.Address() # Address | Address object that needs to be validated.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Address Suggestion
        api_response = api_instance.verify_and_suggest_address(return_suggestions, address, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddressValidationApi->verify_and_suggest_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_suggestions** | **str**| To return suggested addresses, set this to true. | [default to &#39;true&#39;]
 **address** | [**Address**](Address.md)| Address object that needs to be validated. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**AddressSuggestionResponse**](AddressSuggestionResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

