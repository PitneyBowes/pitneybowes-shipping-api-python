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


class DimensionRules(object):
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
        'required': 'bool',
        'unit_of_measurement': 'str',
        'min_parcel_dimensions': 'DimensionRulesMinParcelDimensions',
        'max_parcel_dimensions': 'DimensionRulesMaxParcelDimensions',
        'min_length_plus_girth': 'int',
        'max_length_plus_girth': 'int'
    }

    attribute_map = {
        'required': 'required',
        'unit_of_measurement': 'unitOfMeasurement',
        'min_parcel_dimensions': 'minParcelDimensions',
        'max_parcel_dimensions': 'maxParcelDimensions',
        'min_length_plus_girth': 'minLengthPlusGirth',
        'max_length_plus_girth': 'maxLengthPlusGirth'
    }

    def __init__(self, required=None, unit_of_measurement=None, min_parcel_dimensions=None, max_parcel_dimensions=None, min_length_plus_girth=None, max_length_plus_girth=None, local_vars_configuration=None):  # noqa: E501
        """DimensionRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._required = None
        self._unit_of_measurement = None
        self._min_parcel_dimensions = None
        self._max_parcel_dimensions = None
        self._min_length_plus_girth = None
        self._max_length_plus_girth = None
        self.discriminator = None

        if required is not None:
            self.required = required
        if unit_of_measurement is not None:
            self.unit_of_measurement = unit_of_measurement
        if min_parcel_dimensions is not None:
            self.min_parcel_dimensions = min_parcel_dimensions
        if max_parcel_dimensions is not None:
            self.max_parcel_dimensions = max_parcel_dimensions
        if min_length_plus_girth is not None:
            self.min_length_plus_girth = min_length_plus_girth
        if max_length_plus_girth is not None:
            self.max_length_plus_girth = max_length_plus_girth

    @property
    def required(self):
        """Gets the required of this DimensionRules.  # noqa: E501


        :return: The required of this DimensionRules.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DimensionRules.


        :param required: The required of this DimensionRules.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this DimensionRules.  # noqa: E501


        :return: The unit_of_measurement of this DimensionRules.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this DimensionRules.


        :param unit_of_measurement: The unit_of_measurement of this DimensionRules.  # noqa: E501
        :type: str
        """

        self._unit_of_measurement = unit_of_measurement

    @property
    def min_parcel_dimensions(self):
        """Gets the min_parcel_dimensions of this DimensionRules.  # noqa: E501


        :return: The min_parcel_dimensions of this DimensionRules.  # noqa: E501
        :rtype: DimensionRulesMinParcelDimensions
        """
        return self._min_parcel_dimensions

    @min_parcel_dimensions.setter
    def min_parcel_dimensions(self, min_parcel_dimensions):
        """Sets the min_parcel_dimensions of this DimensionRules.


        :param min_parcel_dimensions: The min_parcel_dimensions of this DimensionRules.  # noqa: E501
        :type: DimensionRulesMinParcelDimensions
        """

        self._min_parcel_dimensions = min_parcel_dimensions

    @property
    def max_parcel_dimensions(self):
        """Gets the max_parcel_dimensions of this DimensionRules.  # noqa: E501


        :return: The max_parcel_dimensions of this DimensionRules.  # noqa: E501
        :rtype: DimensionRulesMaxParcelDimensions
        """
        return self._max_parcel_dimensions

    @max_parcel_dimensions.setter
    def max_parcel_dimensions(self, max_parcel_dimensions):
        """Sets the max_parcel_dimensions of this DimensionRules.


        :param max_parcel_dimensions: The max_parcel_dimensions of this DimensionRules.  # noqa: E501
        :type: DimensionRulesMaxParcelDimensions
        """

        self._max_parcel_dimensions = max_parcel_dimensions

    @property
    def min_length_plus_girth(self):
        """Gets the min_length_plus_girth of this DimensionRules.  # noqa: E501


        :return: The min_length_plus_girth of this DimensionRules.  # noqa: E501
        :rtype: int
        """
        return self._min_length_plus_girth

    @min_length_plus_girth.setter
    def min_length_plus_girth(self, min_length_plus_girth):
        """Sets the min_length_plus_girth of this DimensionRules.


        :param min_length_plus_girth: The min_length_plus_girth of this DimensionRules.  # noqa: E501
        :type: int
        """

        self._min_length_plus_girth = min_length_plus_girth

    @property
    def max_length_plus_girth(self):
        """Gets the max_length_plus_girth of this DimensionRules.  # noqa: E501


        :return: The max_length_plus_girth of this DimensionRules.  # noqa: E501
        :rtype: int
        """
        return self._max_length_plus_girth

    @max_length_plus_girth.setter
    def max_length_plus_girth(self, max_length_plus_girth):
        """Sets the max_length_plus_girth of this DimensionRules.


        :param max_length_plus_girth: The max_length_plus_girth of this DimensionRules.  # noqa: E501
        :type: int
        """

        self._max_length_plus_girth = max_length_plus_girth

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
        if not isinstance(other, DimensionRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DimensionRules):
            return True

        return self.to_dict() != other.to_dict()