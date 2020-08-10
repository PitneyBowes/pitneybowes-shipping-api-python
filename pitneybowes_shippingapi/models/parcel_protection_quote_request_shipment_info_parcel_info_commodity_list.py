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

from pitneybowes_shippingapi.configuration import Configuration


class ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList(object):
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
        'category_path': 'str',
        'item_code': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'category_path': 'categoryPath',
        'item_code': 'itemCode',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, category_path=None, item_code=None, name=None, url=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._category_path = None
        self._item_code = None
        self._name = None
        self._url = None
        self.discriminator = None

        self.category_path = category_path
        self.item_code = item_code
        self.name = name
        self.url = url

    @property
    def category_path(self):
        """Gets the category_path of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501


        :return: The category_path of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :rtype: str
        """
        return self._category_path

    @category_path.setter
    def category_path(self, category_path):
        """Sets the category_path of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.


        :param category_path: The category_path of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category_path is None:  # noqa: E501
            raise ValueError("Invalid value for `category_path`, must not be `None`")  # noqa: E501

        self._category_path = category_path

    @property
    def item_code(self):
        """Gets the item_code of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501


        :return: The item_code of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.


        :param item_code: The item_code of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and item_code is None:  # noqa: E501
            raise ValueError("Invalid value for `item_code`, must not be `None`")  # noqa: E501

        self._item_code = item_code

    @property
    def name(self):
        """Gets the name of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501


        :return: The name of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.


        :param name: The name of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501


        :return: The url of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.


        :param url: The url of this ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityList):
            return True

        return self.to_dict() != other.to_dict()