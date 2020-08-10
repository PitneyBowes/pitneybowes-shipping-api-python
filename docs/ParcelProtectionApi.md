# pitneybowes_shippingapi.ParcelProtectionApi

All URIs are relative to *https://api-qa.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_parcel_protection**](ParcelProtectionApi.md#cancel_parcel_protection) | **POST** /v1/parcel-protection/void | Parcel Protection Coverage
[**get_parcel_protection_coverage**](ParcelProtectionApi.md#get_parcel_protection_coverage) | **POST** /v1/parcel-protection/create | Parcel Protection Coverage
[**get_parcel_protection_quote**](ParcelProtectionApi.md#get_parcel_protection_quote) | **POST** /v1/parcel-protection/quote | Parcel Protection Quote
[**get_parcel_protection_reports**](ParcelProtectionApi.md#get_parcel_protection_reports) | **GET** /v1/parcel-protection/{developerId}/policies | Parcel Protection Reports


# **cancel_parcel_protection**
> VoidParcelProtectionResponse cancel_parcel_protection(x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, x_pb_unified_error_structure=x_pb_unified_error_structure)

Parcel Protection Coverage

This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.

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
    api_instance = pitneybowes_shippingapi.ParcelProtectionApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
parcel_protection_reference_id = 'parcel_protection_reference_id_example' # str | Required. The identifier for the PB Parcel Protection policy that is being voided.
void_parcel_protection_request = {"shipperID":"9024324564","parcelProtectionAccountID":"IPACT2345678"} # VoidParcelProtectionRequest | manifest
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Parcel Protection Coverage
        api_response = api_instance.cancel_parcel_protection(x_pb_transaction_id, parcel_protection_reference_id, void_parcel_protection_request, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParcelProtectionApi->cancel_parcel_protection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **parcel_protection_reference_id** | **str**| Required. The identifier for the PB Parcel Protection policy that is being voided. | 
 **void_parcel_protection_request** | [**VoidParcelProtectionRequest**](VoidParcelProtectionRequest.md)| manifest | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**VoidParcelProtectionResponse**](VoidParcelProtectionResponse.md)

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

# **get_parcel_protection_coverage**
> ParcelProtectionCreateResponse get_parcel_protection_coverage(x_pb_transaction_id, parcel_protection_create_request, x_pb_unified_error_structure=x_pb_unified_error_structure)

Parcel Protection Coverage

This API lets merchants request Pitney Bowes [Parcel Protection](https://shipping.pitneybowes.com/faqs/parcel-protection.html) coverage for shipments. Merchants can request coverage for shipments created with the Shipping APIs as well as for shipments created with other platforms.

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
    api_instance = pitneybowes_shippingapi.ParcelProtectionApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
parcel_protection_create_request = {"shipmentInfo":{"trackingNumber":"940509898641491871138","carrier":"USPS","serviceId":"PM","insuranceCoverageValue":1000,"insuranceCoverageValueCurrency":"USD","parcelInfo":{"commodityList":[{"categoryPath":"electronics","itemCode":"SKU1084","name":"Laptop","url":"https://example.com/computers/laptop/1084"}]},"shipperInfo":{"shipperID":"9024324564","address":{"addressLines":["545 Market St"],"cityTown":"San Francisco","stateProvince":"CA","postalCode":"94105-2847","countryCode":"US"},"companyName":"Supplies","givenName":"John","middleName":"James","familyName":"Smith","email":"john@example.com","phoneNumbers":[{"number":"1234567890","type":"business phone"}]},"consigneeInfo":{"address":{"addressLines":["284 W Fulton"],"cityTown":"Garden City","stateProvince":"KS","postalCode":"67846","countryCode":"US"},"companyName":"Shop","givenName":"Mary","middleName":"Anne","familyName":"Jones","email":"mary@example.com","phoneNumbers":[{"number":"6205551234","type":"business phone"},{"number":"6205554321","type":"fax"}]}}} # ParcelProtectionCreateRequest | manifest
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Parcel Protection Coverage
        api_response = api_instance.get_parcel_protection_coverage(x_pb_transaction_id, parcel_protection_create_request, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParcelProtectionApi->get_parcel_protection_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **parcel_protection_create_request** | [**ParcelProtectionCreateRequest**](ParcelProtectionCreateRequest.md)| manifest | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**ParcelProtectionCreateResponse**](ParcelProtectionCreateResponse.md)

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

# **get_parcel_protection_quote**
> ParcelProtectionQuoteResponse get_parcel_protection_quote(x_pb_transaction_id, parcel_protection_quote_request, x_pb_unified_error_structure=x_pb_unified_error_structure)

Parcel Protection Quote

This API provides a quote for covering a shipment through Pitney Bowes [Parcel Protection](https://www.pitneybowes.com/us/ecommerce-delivery-services/parcel-protection.html).

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
    api_instance = pitneybowes_shippingapi.ParcelProtectionApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
parcel_protection_quote_request = {"shipmentInfo":{"carrier":"USPS","serviceId":"PM","insuranceCoverageValue":1000,"insuranceCoverageValueCurrency":"USD","parcelInfo":{"commodityList":[{"categoryPath":"electronics","itemCode":"SKU1084","name":"Laptop","url":"https://example.com/computers/laptop/1084"}]},"shipperInfo":{"shipperID":"9024324564","address":{"addressLines":["545 Market St"],"cityTown":"San Francisco","stateProvince":"CA","postalCode":"94105-2847","countryCode":"US"}},"consigneeInfo":{"address":{"addressLines":["284 W Fulton"],"cityTown":"Garden City","stateProvince":"KS","postalCode":"67846","countryCode":"US"}}}} # ParcelProtectionQuoteRequest | manifest
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Parcel Protection Quote
        api_response = api_instance.get_parcel_protection_quote(x_pb_transaction_id, parcel_protection_quote_request, x_pb_unified_error_structure=x_pb_unified_error_structure)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParcelProtectionApi->get_parcel_protection_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **parcel_protection_quote_request** | [**ParcelProtectionQuoteRequest**](ParcelProtectionQuoteRequest.md)| manifest | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**ParcelProtectionQuoteResponse**](ParcelProtectionQuoteResponse.md)

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

# **get_parcel_protection_reports**
> ParcelProtectionPolicyResponse get_parcel_protection_reports(x_pb_transaction_id, developer_id, policy_created_from_date, x_pb_unified_error_structure=x_pb_unified_error_structure, policy_created_to_date=policy_created_to_date, policy_reference_id=policy_reference_id, parcel_tracking_number=parcel_tracking_number, merchant_id=merchant_id, policy_status=policy_status, size=size, page=page, sort=sort)

Parcel Protection Reports

This operation retrieves the policy status and other information on the Parcel Protection policies you have purchased for your shipments. Further Details https://shipping.pitneybowes.com/api/get-parcel-protection-reports.html

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
    api_instance = pitneybowes_shippingapi.ParcelProtectionApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
developer_id = 'developer_id_example' # str | Required. Your Pitney Bowes developer ID.
policy_created_from_date = 'policy_created_from_date_example' # str | The beginning of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset.
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
policy_created_to_date = 'policy_created_to_date_example' # str | The end of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset. (optional)
policy_reference_id = 'policy_reference_id_example' # str | The unique identifier for the PB Parcel Protection policy.]. (optional)
parcel_tracking_number = 'parcel_tracking_number_example' # str | The parcel tracking number of the shipment that the policy applies to. (optional)
merchant_id = 'merchant_id_example' # str | The merchant's Shipper ID. This is the value of the postalReportingNumber element in the Merchant Object. (optional)
policy_status = 'policy_status_example' # str | Whether the policy is active or voided. (optional)
size = 'size_example' # str | The number of transactions to return per page in the result set. (optional)
page = 'page_example' # str | The index number of the page to return. Page index numbering starts at 0. Specifying page=0 returns the first page of the result set. (optional)
sort = 'sort_example' # str | Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc). (optional)

    try:
        # Parcel Protection Reports
        api_response = api_instance.get_parcel_protection_reports(x_pb_transaction_id, developer_id, policy_created_from_date, x_pb_unified_error_structure=x_pb_unified_error_structure, policy_created_to_date=policy_created_to_date, policy_reference_id=policy_reference_id, parcel_tracking_number=parcel_tracking_number, merchant_id=merchant_id, policy_status=policy_status, size=size, page=page, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParcelProtectionApi->get_parcel_protection_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **developer_id** | **str**| Required. Your Pitney Bowes developer ID. | 
 **policy_created_from_date** | **str**| The beginning of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **policy_created_to_date** | **str**| The end of the date range. Specify this value in UTC using the ISO 8601 standard. You must include both date and time, and you must end the time with Z to indicate a zero offset. | [optional] 
 **policy_reference_id** | **str**| The unique identifier for the PB Parcel Protection policy.]. | [optional] 
 **parcel_tracking_number** | **str**| The parcel tracking number of the shipment that the policy applies to. | [optional] 
 **merchant_id** | **str**| The merchant&#39;s Shipper ID. This is the value of the postalReportingNumber element in the Merchant Object. | [optional] 
 **policy_status** | **str**| Whether the policy is active or voided. | [optional] 
 **size** | **str**| The number of transactions to return per page in the result set. | [optional] 
 **page** | **str**| The index number of the page to return. Page index numbering starts at 0. Specifying page&#x3D;0 returns the first page of the result set. | [optional] 
 **sort** | **str**| Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc). | [optional] 

### Return type

[**ParcelProtectionPolicyResponse**](ParcelProtectionPolicyResponse.md)

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

