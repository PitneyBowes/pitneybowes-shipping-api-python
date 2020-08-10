# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pitneybowes_shippingapi
from pitneybowes_shippingapi.models.parcel_protection_policy_response_sort import ParcelProtectionPolicyResponseSort  # noqa: E501
from pitneybowes_shippingapi.rest import ApiException

class TestParcelProtectionPolicyResponseSort(unittest.TestCase):
    """ParcelProtectionPolicyResponseSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionPolicyResponseSort
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pitneybowes_shippingapi.models.parcel_protection_policy_response_sort.ParcelProtectionPolicyResponseSort()  # noqa: E501
        if include_optional :
            return ParcelProtectionPolicyResponseSort(
                direction = '0', 
                _property = '0', 
                ignore_case = True, 
                null_handling = '0', 
                descending = True, 
                ascending = True
            )
        else :
            return ParcelProtectionPolicyResponseSort(
        )

    def testParcelProtectionPolicyResponseSort(self):
        """Test ParcelProtectionPolicyResponseSort"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()