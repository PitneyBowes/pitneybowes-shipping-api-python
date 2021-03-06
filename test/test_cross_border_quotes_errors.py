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
from pbshipping.models.cross_border_quotes_errors import CrossBorderQuotesErrors  # noqa: E501
from pbshipping.rest import ApiException

class TestCrossBorderQuotesErrors(unittest.TestCase):
    """CrossBorderQuotesErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesErrors
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.cross_border_quotes_errors.CrossBorderQuotesErrors()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesErrors(
                quote = [
                    pbshipping.models.cross_border_quotes_errors_quote.CrossBorderQuotesErrors_quote(
                        quote_currency = '0', 
                        quote_lines = [
                            pbshipping.models.cross_border_quotes_errors_quote_lines.CrossBorderQuotesErrors_quoteLines(
                                line_id = '0', 
                                merchant_com_ref_id = '0', 
                                quantity = 56, 
                                unit_errors = [
                                    pbshipping.models.cross_border_quotes_errors_unit_errors.CrossBorderQuotesErrors_unitErrors(
                                        error = 56, 
                                        message = '0', )
                                    ], )
                            ], 
                        errors = pbshipping.models.cross_border_quotes_errors_errors.CrossBorderQuotesErrors_errors(), )
                    ]
            )
        else :
            return CrossBorderQuotesErrors(
        )

    def testCrossBorderQuotesErrors(self):
        """Test CrossBorderQuotesErrors"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
