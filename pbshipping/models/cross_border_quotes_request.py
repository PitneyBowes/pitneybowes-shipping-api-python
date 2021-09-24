# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pbshipping.configuration import Configuration


class CrossBorderQuotesRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'quote_currency': 'str',
        'basket_currency': 'str',
        'from_address': 'Address',
        'to_address': 'Address',
        'basket_items': 'list[CrossBorderQuotesRequestBasketItems]',
        'rates': 'list[CrossBorderQuotesRequestRates]',
        'shipment_options': 'list[CarrierFacilityResponseCarrierFacilityOptions]'
    }

    attribute_map = {
        'quote_currency': 'quoteCurrency',
        'basket_currency': 'basketCurrency',
        'from_address': 'fromAddress',
        'to_address': 'toAddress',
        'basket_items': 'basketItems',
        'rates': 'rates',
        'shipment_options': 'shipmentOptions'
    }

    def __init__(self, quote_currency=None, basket_currency=None, from_address=None, to_address=None, basket_items=None, rates=None, shipment_options=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._quote_currency = None
        self._basket_currency = None
        self._from_address = None
        self._to_address = None
        self._basket_items = None
        self._rates = None
        self._shipment_options = None
        self.discriminator = None

        self.quote_currency = quote_currency
        self.basket_currency = basket_currency
        if from_address is not None:
            self.from_address = from_address
        self.to_address = to_address
        self.basket_items = basket_items
        self.rates = rates
        if shipment_options is not None:
            self.shipment_options = shipment_options

    @property
    def quote_currency(self):
        """Gets the quote_currency of this CrossBorderQuotesRequest.  # noqa: E501

        The currency to return the quote in. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR  # noqa: E501

        :return: The quote_currency of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this CrossBorderQuotesRequest.

        The currency to return the quote in. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR  # noqa: E501

        :param quote_currency: The quote_currency of this CrossBorderQuotesRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and quote_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `quote_currency`, must not be `None`")  # noqa: E501

        self._quote_currency = quote_currency

    @property
    def basket_currency(self):
        """Gets the basket_currency of this CrossBorderQuotesRequest.  # noqa: E501

        The default currency of the basket. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR  # noqa: E501

        :return: The basket_currency of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: str
        """
        return self._basket_currency

    @basket_currency.setter
    def basket_currency(self, basket_currency):
        """Sets the basket_currency of this CrossBorderQuotesRequest.

        The default currency of the basket. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR  # noqa: E501

        :param basket_currency: The basket_currency of this CrossBorderQuotesRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and basket_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `basket_currency`, must not be `None`")  # noqa: E501

        self._basket_currency = basket_currency

    @property
    def from_address(self):
        """Gets the from_address of this CrossBorderQuotesRequest.  # noqa: E501


        :return: The from_address of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: Address
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this CrossBorderQuotesRequest.


        :param from_address: The from_address of this CrossBorderQuotesRequest.  # noqa: E501
        :type: Address
        """

        self._from_address = from_address

    @property
    def to_address(self):
        """Gets the to_address of this CrossBorderQuotesRequest.  # noqa: E501


        :return: The to_address of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: Address
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """Sets the to_address of this CrossBorderQuotesRequest.


        :param to_address: The to_address of this CrossBorderQuotesRequest.  # noqa: E501
        :type: Address
        """
        if self.local_vars_configuration.client_side_validation and to_address is None:  # noqa: E501
            raise ValueError("Invalid value for `to_address`, must not be `None`")  # noqa: E501

        self._to_address = to_address

    @property
    def basket_items(self):
        """Gets the basket_items of this CrossBorderQuotesRequest.  # noqa: E501

        The items in the buyer's shopping basket.  # noqa: E501

        :return: The basket_items of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: list[CrossBorderQuotesRequestBasketItems]
        """
        return self._basket_items

    @basket_items.setter
    def basket_items(self, basket_items):
        """Sets the basket_items of this CrossBorderQuotesRequest.

        The items in the buyer's shopping basket.  # noqa: E501

        :param basket_items: The basket_items of this CrossBorderQuotesRequest.  # noqa: E501
        :type: list[CrossBorderQuotesRequestBasketItems]
        """
        if self.local_vars_configuration.client_side_validation and basket_items is None:  # noqa: E501
            raise ValueError("Invalid value for `basket_items`, must not be `None`")  # noqa: E501

        self._basket_items = basket_items

    @property
    def rates(self):
        """Gets the rates of this CrossBorderQuotesRequest.  # noqa: E501

        Specifies the carrier, service, parcel, and other information. In a response, this field also contains the service charges. Importatn- In a request, the rates array can contain only one rates object.  # noqa: E501

        :return: The rates of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: list[CrossBorderQuotesRequestRates]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this CrossBorderQuotesRequest.

        Specifies the carrier, service, parcel, and other information. In a response, this field also contains the service charges. Importatn- In a request, the rates array can contain only one rates object.  # noqa: E501

        :param rates: The rates of this CrossBorderQuotesRequest.  # noqa: E501
        :type: list[CrossBorderQuotesRequestRates]
        """
        if self.local_vars_configuration.client_side_validation and rates is None:  # noqa: E501
            raise ValueError("Invalid value for `rates`, must not be `None`")  # noqa: E501

        self._rates = rates

    @property
    def shipment_options(self):
        """Gets the shipment_options of this CrossBorderQuotesRequest.  # noqa: E501


        :return: The shipment_options of this CrossBorderQuotesRequest.  # noqa: E501
        :rtype: list[CarrierFacilityResponseCarrierFacilityOptions]
        """
        return self._shipment_options

    @shipment_options.setter
    def shipment_options(self, shipment_options):
        """Sets the shipment_options of this CrossBorderQuotesRequest.


        :param shipment_options: The shipment_options of this CrossBorderQuotesRequest.  # noqa: E501
        :type: list[CarrierFacilityResponseCarrierFacilityOptions]
        """

        self._shipment_options = shipment_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CrossBorderQuotesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesRequest):
            return True

        return self.to_dict() != other.to_dict()