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


class DeliveryCommitment(object):
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
        'additional_details': 'str',
        'estimated_delivery_date_time': 'str',
        'guarantee': 'str',
        'max_estimated_number_of_days': 'str',
        'min_estimated_number_of_days': 'str'
    }

    attribute_map = {
        'additional_details': 'additionalDetails',
        'estimated_delivery_date_time': 'estimatedDeliveryDateTime',
        'guarantee': 'guarantee',
        'max_estimated_number_of_days': 'maxEstimatedNumberOfDays',
        'min_estimated_number_of_days': 'minEstimatedNumberOfDays'
    }

    def __init__(self, additional_details=None, estimated_delivery_date_time=None, guarantee=None, max_estimated_number_of_days=None, min_estimated_number_of_days=None, local_vars_configuration=None):  # noqa: E501
        """DeliveryCommitment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_details = None
        self._estimated_delivery_date_time = None
        self._guarantee = None
        self._max_estimated_number_of_days = None
        self._min_estimated_number_of_days = None
        self.discriminator = None

        if additional_details is not None:
            self.additional_details = additional_details
        if estimated_delivery_date_time is not None:
            self.estimated_delivery_date_time = estimated_delivery_date_time
        if guarantee is not None:
            self.guarantee = guarantee
        if max_estimated_number_of_days is not None:
            self.max_estimated_number_of_days = max_estimated_number_of_days
        if min_estimated_number_of_days is not None:
            self.min_estimated_number_of_days = min_estimated_number_of_days

    @property
    def additional_details(self):
        """Gets the additional_details of this DeliveryCommitment.  # noqa: E501


        :return: The additional_details of this DeliveryCommitment.  # noqa: E501
        :rtype: str
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """Sets the additional_details of this DeliveryCommitment.


        :param additional_details: The additional_details of this DeliveryCommitment.  # noqa: E501
        :type: str
        """

        self._additional_details = additional_details

    @property
    def estimated_delivery_date_time(self):
        """Gets the estimated_delivery_date_time of this DeliveryCommitment.  # noqa: E501


        :return: The estimated_delivery_date_time of this DeliveryCommitment.  # noqa: E501
        :rtype: str
        """
        return self._estimated_delivery_date_time

    @estimated_delivery_date_time.setter
    def estimated_delivery_date_time(self, estimated_delivery_date_time):
        """Sets the estimated_delivery_date_time of this DeliveryCommitment.


        :param estimated_delivery_date_time: The estimated_delivery_date_time of this DeliveryCommitment.  # noqa: E501
        :type: str
        """

        self._estimated_delivery_date_time = estimated_delivery_date_time

    @property
    def guarantee(self):
        """Gets the guarantee of this DeliveryCommitment.  # noqa: E501


        :return: The guarantee of this DeliveryCommitment.  # noqa: E501
        :rtype: str
        """
        return self._guarantee

    @guarantee.setter
    def guarantee(self, guarantee):
        """Sets the guarantee of this DeliveryCommitment.


        :param guarantee: The guarantee of this DeliveryCommitment.  # noqa: E501
        :type: str
        """

        self._guarantee = guarantee

    @property
    def max_estimated_number_of_days(self):
        """Gets the max_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501


        :return: The max_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_number_of_days

    @max_estimated_number_of_days.setter
    def max_estimated_number_of_days(self, max_estimated_number_of_days):
        """Sets the max_estimated_number_of_days of this DeliveryCommitment.


        :param max_estimated_number_of_days: The max_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501
        :type: str
        """

        self._max_estimated_number_of_days = max_estimated_number_of_days

    @property
    def min_estimated_number_of_days(self):
        """Gets the min_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501


        :return: The min_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_number_of_days

    @min_estimated_number_of_days.setter
    def min_estimated_number_of_days(self, min_estimated_number_of_days):
        """Sets the min_estimated_number_of_days of this DeliveryCommitment.


        :param min_estimated_number_of_days: The min_estimated_number_of_days of this DeliveryCommitment.  # noqa: E501
        :type: str
        """

        self._min_estimated_number_of_days = min_estimated_number_of_days

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
        if not isinstance(other, DeliveryCommitment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryCommitment):
            return True

        return self.to_dict() != other.to_dict()
