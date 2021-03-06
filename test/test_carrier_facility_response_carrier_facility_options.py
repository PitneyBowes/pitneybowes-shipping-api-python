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

import pbshipping
from pbshipping.models.carrier_facility_response_carrier_facility_options import CarrierFacilityResponseCarrierFacilityOptions  # noqa: E501
from pbshipping.rest import ApiException

class TestCarrierFacilityResponseCarrierFacilityOptions(unittest.TestCase):
    """CarrierFacilityResponseCarrierFacilityOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CarrierFacilityResponseCarrierFacilityOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.carrier_facility_response_carrier_facility_options.CarrierFacilityResponseCarrierFacilityOptions()  # noqa: E501
        if include_optional :
            return CarrierFacilityResponseCarrierFacilityOptions(
                name = '0', 
                value = '0'
            )
        else :
            return CarrierFacilityResponseCarrierFacilityOptions(
        )

    def testCarrierFacilityResponseCarrierFacilityOptions(self):
        """Test CarrierFacilityResponseCarrierFacilityOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
