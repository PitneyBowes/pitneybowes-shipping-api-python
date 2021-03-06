# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pbshipping.api_client import ApiClient
from pbshipping.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CrossBorderQuotesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cross_border_quotes(self, cross_border_quotes_request, **kwargs):  # noqa: E501
        """Cross-Border Quotes  # noqa: E501

        This operation provides an estimate of the duties, taxes, and transportation costs for the items in a buyer's online shopping basket. The API calculates how many separate parcels are required to ship the items and estimates costs. The API checks each item's eligibility to clear customs and returns the quote for eligible items. To look for futher info please look into [Cross-Border Quotes](https://shipping.pitneybowes.com/api/post-quotes.html#)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cross_border_quotes(cross_border_quotes_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CrossBorderQuotesRequest cross_border_quotes_request: (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CrossBorderQuotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_cross_border_quotes_with_http_info(cross_border_quotes_request, **kwargs)  # noqa: E501

    def get_cross_border_quotes_with_http_info(self, cross_border_quotes_request, **kwargs):  # noqa: E501
        """Cross-Border Quotes  # noqa: E501

        This operation provides an estimate of the duties, taxes, and transportation costs for the items in a buyer's online shopping basket. The API calculates how many separate parcels are required to ship the items and estimates costs. The API checks each item's eligibility to clear customs and returns the quote for eligible items. To look for futher info please look into [Cross-Border Quotes](https://shipping.pitneybowes.com/api/post-quotes.html#)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cross_border_quotes_with_http_info(cross_border_quotes_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CrossBorderQuotesRequest cross_border_quotes_request: (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CrossBorderQuotesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'cross_border_quotes_request',
            'x_pb_unified_error_structure'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cross_border_quotes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cross_border_quotes_request' is set
        if self.api_client.client_side_validation and ('cross_border_quotes_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['cross_border_quotes_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cross_border_quotes_request` when calling `get_cross_border_quotes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cross_border_quotes_request' in local_var_params:
            body_params = local_var_params['cross_border_quotes_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/crossborder/checkout/quotes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CrossBorderQuotesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def predicted_hs_code(self, x_pb_transaction_id, manifest, **kwargs):  # noqa: E501
        """Predicts the HS Code for a parcel  # noqa: E501

        This operation predicts the HS Code for a parcel being shipped internationally and gives the level of confidence in the prediction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predicted_hs_code(x_pb_transaction_id, manifest, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param Manifest manifest: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ParcelProtectionPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.predicted_hs_code_with_http_info(x_pb_transaction_id, manifest, **kwargs)  # noqa: E501

    def predicted_hs_code_with_http_info(self, x_pb_transaction_id, manifest, **kwargs):  # noqa: E501
        """Predicts the HS Code for a parcel  # noqa: E501

        This operation predicts the HS Code for a parcel being shipped internationally and gives the level of confidence in the prediction.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.predicted_hs_code_with_http_info(x_pb_transaction_id, manifest, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_pb_transaction_id: Required. A unique identifier for the transaction, up to 25 characters. (required)
        :param Manifest manifest: manifest (required)
        :param bool x_pb_unified_error_structure: Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ParcelProtectionPolicyResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_pb_transaction_id',
            'manifest',
            'x_pb_unified_error_structure'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method predicted_hs_code" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_pb_transaction_id' is set
        if self.api_client.client_side_validation and ('x_pb_transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_pb_transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_pb_transaction_id` when calling `predicted_hs_code`")  # noqa: E501
        # verify the required parameter 'manifest' is set
        if self.api_client.client_side_validation and ('manifest' not in local_var_params or  # noqa: E501
                                                        local_var_params['manifest'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `manifest` when calling `predicted_hs_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_pb_unified_error_structure' in local_var_params:
            header_params['X-PB-UnifiedErrorStructure'] = local_var_params['x_pb_unified_error_structure']  # noqa: E501
        if 'x_pb_transaction_id' in local_var_params:
            header_params['X-PB-TransactionId'] = local_var_params['x_pb_transaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'manifest' in local_var_params:
            body_params = local_var_params['manifest']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/v1/crossborder/hs-classification/items', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParcelProtectionPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
