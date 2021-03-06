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
from pbshipping.models.parcel_protection_create_request import ParcelProtectionCreateRequest  # noqa: E501
from pbshipping.rest import ApiException

class TestParcelProtectionCreateRequest(unittest.TestCase):
    """ParcelProtectionCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.parcel_protection_create_request.ParcelProtectionCreateRequest()  # noqa: E501
        if include_optional :
            return ParcelProtectionCreateRequest(
                parcel_protection_account_id = '0', 
                parcel_protection_program_id = '0', 
                shipment_info = pbshipping.models.parcel_protection_create_request_shipment_info.ParcelProtectionCreateRequest_shipmentInfo(
                    tracking_number = '0', 
                    carrier = '0', 
                    service_id = '0', 
                    insurance_coverage_value = 56, 
                    insurance_coverage_value_currency = '0', 
                    parcel_info = pbshipping.models.parcel_protection_create_request_shipment_info_parcel_info.ParcelProtectionCreateRequest_shipmentInfo_parcelInfo(
                        commodity_list = [
                            pbshipping.models.parcel_protection_create_request_shipment_info_parcel_info_commodity_list.ParcelProtectionCreateRequest_shipmentInfo_parcelInfo_commodityList(
                                category_path = '0', 
                                item_code = '0', 
                                name = '0', 
                                url = '0', )
                            ], ), 
                    shipper_info = pbshipping.models.parcel_protection_create_request_shipment_info_shipper_info.ParcelProtectionCreateRequest_shipmentInfo_shipperInfo(
                        shipper_id = '0', 
                        address = pbshipping.models.parcel_protection_create_request_shipment_info_shipper_info_address.ParcelProtectionCreateRequest_shipmentInfo_shipperInfo_address(
                            address_lines = [
                                '0'
                                ], 
                            city_town = '0', 
                            state_province = '0', 
                            postal_code = '0', 
                            country_code = '0', ), 
                        company_name = '0', 
                        family_name = '0', 
                        given_name = '0', 
                        middle_name = '0', 
                        email = '0', 
                        phone_numbers = [
                            None
                            ], ), 
                    consignee_info = pbshipping.models.parcel_protection_create_request_shipment_info_consignee_info.ParcelProtectionCreateRequest_shipmentInfo_consigneeInfo(
                        company_name = '0', 
                        family_name = '0', 
                        given_name = '0', 
                        middle_name = '0', 
                        email = '0', ), )
            )
        else :
            return ParcelProtectionCreateRequest(
        )

    def testParcelProtectionCreateRequest(self):
        """Test ParcelProtectionCreateRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
