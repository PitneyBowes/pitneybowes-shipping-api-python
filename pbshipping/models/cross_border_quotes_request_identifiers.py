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


class CrossBorderQuotesRequestIdentifiers(object):
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
        'number': 'str',
        'source': 'str'
    }

    attribute_map = {
        'number': 'number',
        'source': 'source'
    }

    def __init__(self, number=None, source=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesRequestIdentifiers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._number = None
        self._source = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if source is not None:
            self.source = source

    @property
    def number(self):
        """Gets the number of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501


        :return: The number of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CrossBorderQuotesRequestIdentifiers.


        :param number: The number of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def source(self):
        """Gets the source of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501


        :return: The source of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CrossBorderQuotesRequestIdentifiers.


        :param source: The source of this CrossBorderQuotesRequestIdentifiers.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if not isinstance(other, CrossBorderQuotesRequestIdentifiers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesRequestIdentifiers):
            return True

        return self.to_dict() != other.to_dict()