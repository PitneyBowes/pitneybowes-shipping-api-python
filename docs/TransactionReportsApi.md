# pitneybowes_shippingapi.TransactionReportsApi

All URIs are relative to *https://api-qa.pitneybowes.com/shippingservices*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_report**](TransactionReportsApi.md#get_transaction_report) | **GET** /v4/ledger/developers/{developerId}/transactions/reports | This operation retrieves all transactions for a specified period of time.


# **get_transaction_report**
> PageRealTransactionDetailReport get_transaction_report(developer_id, x_pb_unified_error_structure=x_pb_unified_error_structure, from_date=from_date, ship_details=ship_details, page=page, size=size, print_status=print_status, to_date=to_date, transaction_type=transaction_type, merchant_id=merchant_id, sort=sort, parcel_tracking_number=parcel_tracking_number, transaction_id=transaction_id)

This operation retrieves all transactions for a specified period of time.

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
    api_instance = pitneybowes_shippingapi.TransactionReportsApi(api_client)
    developer_id = 'developer_id_example' # str | developerId
x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
from_date = '2013-10-20T19:20:30+01:00' # datetime | fromDate (optional)
ship_details = 0 # int |  (optional) (default to 0)
page = 56 # int |  (optional)
size = 20 # int |  (optional) (default to 20)
print_status = 'print_status_example' # str | printStatus (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | toDate (optional)
transaction_type = 'transaction_type_example' # str | transactionType (optional)
merchant_id = 'merchant_id_example' # str | The value of the postalReportingNumber element in the [merchant object](https://shipping.pitneybowes.com/reference/resource-objects.html). This value is also the merchant's Shipper ID. (optional)
sort = 'sort_example' # str | Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc). Use the following form-  * **sort=<property_name>,<sort_direction>** For example- **sort=transactionId,desc**  (optional)
parcel_tracking_number = 'parcel_tracking_number_example' # str | Parcel tracking number of the shipment. (optional)
transaction_id = 'transaction_id_example' # str | The unique string that identifies all the transactions associated with a given shipment. The string comprises the developer ID and the shipment's X-PB-TransactionId, separated by an underscore (_). For example-  * **transactionId=44397664_ad5aa07-ad7414-a78a-c22b3** (optional)

    try:
        # This operation retrieves all transactions for a specified period of time.
        api_response = api_instance.get_transaction_report(developer_id, x_pb_unified_error_structure=x_pb_unified_error_structure, from_date=from_date, ship_details=ship_details, page=page, size=size, print_status=print_status, to_date=to_date, transaction_type=transaction_type, merchant_id=merchant_id, sort=sort, parcel_tracking_number=parcel_tracking_number, transaction_id=transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionReportsApi->get_transaction_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_id** | **str**| developerId | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **from_date** | **datetime**| fromDate | [optional] 
 **ship_details** | **int**|  | [optional] [default to 0]
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] [default to 20]
 **print_status** | **str**| printStatus | [optional] 
 **to_date** | **datetime**| toDate | [optional] 
 **transaction_type** | **str**| transactionType | [optional] 
 **merchant_id** | **str**| The value of the postalReportingNumber element in the [merchant object](https://shipping.pitneybowes.com/reference/resource-objects.html). This value is also the merchant&#39;s Shipper ID. | [optional] 
 **sort** | **str**| Defines a property to sort on and the sort order. Sort order can be ascending (asc) or descending (desc). Use the following form-  * **sort&#x3D;&lt;property_name&gt;,&lt;sort_direction&gt;** For example- **sort&#x3D;transactionId,desc**  | [optional] 
 **parcel_tracking_number** | **str**| Parcel tracking number of the shipment. | [optional] 
 **transaction_id** | **str**| The unique string that identifies all the transactions associated with a given shipment. The string comprises the developer ID and the shipment&#39;s X-PB-TransactionId, separated by an underscore (_). For example-  * **transactionId&#x3D;44397664_ad5aa07-ad7414-a78a-c22b3** | [optional] 

### Return type

[**PageRealTransactionDetailReport**](PageRealTransactionDetailReport.md)

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

