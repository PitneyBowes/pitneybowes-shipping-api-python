# pitneybowes_shippingapi.ManifestsApi

All URIs are relative to *https://api-qa.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manifest**](ManifestsApi.md#create_manifest) | **POST** /v1/manifests | This operation creates an end-of-day manifest
[**reprint_manifest**](ManifestsApi.md#reprint_manifest) | **GET** /v1/manifests/{manifestId} | reprintManifest
[**retry_manifest**](ManifestsApi.md#retry_manifest) | **GET** /v1/manifests | retryManifest


# **create_manifest**
> Manifest create_manifest(x_pb_transaction_id, manifest, x_pb_unified_error_structure=x_pb_unified_error_structure)

This operation creates an end-of-day manifest

This operation creates an end-of-day manifest that either combines all parcels into a single form or electronically closes the day, depending on the carrier. Use the instructions appropriate to the carrier. * Create a [USPS SCAN Form](https://shipping.pitneybowes.com/api/post-manifests-scan.html)  * Create a [Newgistics Closeout](https://shipping.pitneybowes.com/api/post-manifests-newgistics.html) * Create a [PB Presort Pickup Slip](https://shipping.pitneybowes.com/api/post-manifests-presort.html) * Create a [Manifest for PMOD Shipments](https://shipping.pitneybowes.com/api/post-manifests-pmod.html)

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
    api_instance = pitneybowes_shippingapi.ManifestsApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
manifest = {"carrier":"usps","parcelTrackingNumbers":["9405509898644518132830"],"submissionDate":"2020-07-08","fromAddress":{"company":"Pitney Bowes Inc.","name":"sender_fname","phone":"2032032033","email":"sender@email.com","residential":true,"addressLines":["27 Waterview Drive"],"cityTown":"Shelton","stateProvince":"CT","postalCode":"06484","countryCode":"US"}} # Manifest | manifest
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # This operation creates an end-of-day manifest
        api_response = api_instance.create_manifest(x_pb_transaction_id, manifest, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManifestsApi->create_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **manifest** | [**Manifest**](Manifest.md)| manifest | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**Manifest**](Manifest.md)

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

# **reprint_manifest**
> Manifest reprint_manifest(manifest_id, x_pb_unified_error_structure=x_pb_unified_error_structure)

reprintManifest

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
    api_instance = pitneybowes_shippingapi.ManifestsApi(api_client)
    manifest_id = 'manifest_id_example' # str | manifestId
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # reprintManifest
        api_response = api_instance.reprint_manifest(manifest_id, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManifestsApi->reprint_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **str**| manifestId | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**Manifest**](Manifest.md)

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

# **retry_manifest**
> Manifest retry_manifest(original_transaction_id, x_pb_unified_error_structure=x_pb_unified_error_structure)

retryManifest

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
    api_instance = pitneybowes_shippingapi.ManifestsApi(api_client)
    original_transaction_id = 'original_transaction_id_example' # str | 
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # retryManifest
        api_response = api_instance.retry_manifest(original_transaction_id, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ManifestsApi->retry_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_transaction_id** | **str**|  | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**Manifest**](Manifest.md)

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

