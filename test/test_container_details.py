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
from pbshipping.models.container_details import ContainerDetails  # noqa: E501
from pbshipping.rest import ApiException

class TestContainerDetails(unittest.TestCase):
    """ContainerDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContainerDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.container_details.ContainerDetails()  # noqa: E501
        if include_optional :
            return ContainerDetails(
                commodity_info = [
                    pbshipping.models.commodity_info.CommodityInfo(
                        cargo_air_craft = True, 
                        hazard_class = '0', 
                        infectious_substance_contact = pbshipping.models.infectious_substance_contact.InfectiousSubstanceContact(
                            company_name = '0', 
                            contact_id = '0', 
                            email_address = '0', 
                            person_name = '0', 
                            phone_number = '0', ), 
                        inner_receptacles_quantity = 56, 
                        inner_receptacles_quantity_uom = '0', 
                        packaging_group = '0', 
                        packaging_instructions = '0', 
                        percentage = 1.337, 
                        proper_shipping_name = '0', 
                        quantity = 56, 
                        quantity_uom = '0', 
                        radio_activity_detail = pbshipping.models.radio_activity_detail.RadioActivityDetail(
                            criticality_safety_index = 1.337, 
                            radio_active_parcel_dimension = pbshipping.models.radio_active_parcel_dimension.RadioActiveParcelDimension(
                                uom = 'CM', 
                                height = 1.337, 
                                length = 1.337, 
                                width = 1.337, ), 
                            surface_reading = 1.337, 
                            transport_index = 1.337, ), 
                        radio_nuclide_detail = pbshipping.models.radio_nuclide_detail.RadioNuclideDetail(
                            chemical_form = '0', 
                            expected_package_reportable_quantity = True, 
                            physical_form = '0', 
                            radio_nuclide = '0', 
                            radio_nuclide_activity_uom = '0', 
                            radio_nuclide_activity_value = 1.337, ), 
                        reportable_quantity = True, 
                        technical_name = '0', 
                        un_id = '0', )
                    ], 
                container_type = '0', 
                packaging_type = '0'
            )
        else :
            return ContainerDetails(
        )

    def testContainerDetails(self):
        """Test ContainerDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
