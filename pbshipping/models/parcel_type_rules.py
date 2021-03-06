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


class ParcelTypeRules(object):
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
        'parcel_type': 'ParcelType',
        'branded_name': 'str',
        'rate_type_id': 'str',
        'rate_type_branded_name': 'str',
        'trackable': 'Trackable',
        'special_services_rule': 'list[SpecialServicesRule]',
        'weight_rules': 'list[WeightRules]',
        'dimension_rules': 'list[DimensionRules]',
        'suggested_trackable_special_service_id': 'SpecialServiceCodes'
    }

    attribute_map = {
        'parcel_type': 'parcelType',
        'branded_name': 'brandedName',
        'rate_type_id': 'rateTypeId',
        'rate_type_branded_name': 'rateTypeBrandedName',
        'trackable': 'trackable',
        'special_services_rule': 'specialServicesRule',
        'weight_rules': 'weightRules',
        'dimension_rules': 'dimensionRules',
        'suggested_trackable_special_service_id': 'suggestedTrackableSpecialServiceId'
    }

    def __init__(self, parcel_type=None, branded_name=None, rate_type_id=None, rate_type_branded_name=None, trackable=None, special_services_rule=None, weight_rules=None, dimension_rules=None, suggested_trackable_special_service_id=None, local_vars_configuration=None):  # noqa: E501
        """ParcelTypeRules - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parcel_type = None
        self._branded_name = None
        self._rate_type_id = None
        self._rate_type_branded_name = None
        self._trackable = None
        self._special_services_rule = None
        self._weight_rules = None
        self._dimension_rules = None
        self._suggested_trackable_special_service_id = None
        self.discriminator = None

        if parcel_type is not None:
            self.parcel_type = parcel_type
        if branded_name is not None:
            self.branded_name = branded_name
        if rate_type_id is not None:
            self.rate_type_id = rate_type_id
        if rate_type_branded_name is not None:
            self.rate_type_branded_name = rate_type_branded_name
        if trackable is not None:
            self.trackable = trackable
        if special_services_rule is not None:
            self.special_services_rule = special_services_rule
        if weight_rules is not None:
            self.weight_rules = weight_rules
        if dimension_rules is not None:
            self.dimension_rules = dimension_rules
        if suggested_trackable_special_service_id is not None:
            self.suggested_trackable_special_service_id = suggested_trackable_special_service_id

    @property
    def parcel_type(self):
        """Gets the parcel_type of this ParcelTypeRules.  # noqa: E501


        :return: The parcel_type of this ParcelTypeRules.  # noqa: E501
        :rtype: ParcelType
        """
        return self._parcel_type

    @parcel_type.setter
    def parcel_type(self, parcel_type):
        """Sets the parcel_type of this ParcelTypeRules.


        :param parcel_type: The parcel_type of this ParcelTypeRules.  # noqa: E501
        :type: ParcelType
        """

        self._parcel_type = parcel_type

    @property
    def branded_name(self):
        """Gets the branded_name of this ParcelTypeRules.  # noqa: E501


        :return: The branded_name of this ParcelTypeRules.  # noqa: E501
        :rtype: str
        """
        return self._branded_name

    @branded_name.setter
    def branded_name(self, branded_name):
        """Sets the branded_name of this ParcelTypeRules.


        :param branded_name: The branded_name of this ParcelTypeRules.  # noqa: E501
        :type: str
        """

        self._branded_name = branded_name

    @property
    def rate_type_id(self):
        """Gets the rate_type_id of this ParcelTypeRules.  # noqa: E501


        :return: The rate_type_id of this ParcelTypeRules.  # noqa: E501
        :rtype: str
        """
        return self._rate_type_id

    @rate_type_id.setter
    def rate_type_id(self, rate_type_id):
        """Sets the rate_type_id of this ParcelTypeRules.


        :param rate_type_id: The rate_type_id of this ParcelTypeRules.  # noqa: E501
        :type: str
        """

        self._rate_type_id = rate_type_id

    @property
    def rate_type_branded_name(self):
        """Gets the rate_type_branded_name of this ParcelTypeRules.  # noqa: E501


        :return: The rate_type_branded_name of this ParcelTypeRules.  # noqa: E501
        :rtype: str
        """
        return self._rate_type_branded_name

    @rate_type_branded_name.setter
    def rate_type_branded_name(self, rate_type_branded_name):
        """Sets the rate_type_branded_name of this ParcelTypeRules.


        :param rate_type_branded_name: The rate_type_branded_name of this ParcelTypeRules.  # noqa: E501
        :type: str
        """

        self._rate_type_branded_name = rate_type_branded_name

    @property
    def trackable(self):
        """Gets the trackable of this ParcelTypeRules.  # noqa: E501


        :return: The trackable of this ParcelTypeRules.  # noqa: E501
        :rtype: Trackable
        """
        return self._trackable

    @trackable.setter
    def trackable(self, trackable):
        """Sets the trackable of this ParcelTypeRules.


        :param trackable: The trackable of this ParcelTypeRules.  # noqa: E501
        :type: Trackable
        """

        self._trackable = trackable

    @property
    def special_services_rule(self):
        """Gets the special_services_rule of this ParcelTypeRules.  # noqa: E501


        :return: The special_services_rule of this ParcelTypeRules.  # noqa: E501
        :rtype: list[SpecialServicesRule]
        """
        return self._special_services_rule

    @special_services_rule.setter
    def special_services_rule(self, special_services_rule):
        """Sets the special_services_rule of this ParcelTypeRules.


        :param special_services_rule: The special_services_rule of this ParcelTypeRules.  # noqa: E501
        :type: list[SpecialServicesRule]
        """

        self._special_services_rule = special_services_rule

    @property
    def weight_rules(self):
        """Gets the weight_rules of this ParcelTypeRules.  # noqa: E501


        :return: The weight_rules of this ParcelTypeRules.  # noqa: E501
        :rtype: list[WeightRules]
        """
        return self._weight_rules

    @weight_rules.setter
    def weight_rules(self, weight_rules):
        """Sets the weight_rules of this ParcelTypeRules.


        :param weight_rules: The weight_rules of this ParcelTypeRules.  # noqa: E501
        :type: list[WeightRules]
        """

        self._weight_rules = weight_rules

    @property
    def dimension_rules(self):
        """Gets the dimension_rules of this ParcelTypeRules.  # noqa: E501


        :return: The dimension_rules of this ParcelTypeRules.  # noqa: E501
        :rtype: list[DimensionRules]
        """
        return self._dimension_rules

    @dimension_rules.setter
    def dimension_rules(self, dimension_rules):
        """Sets the dimension_rules of this ParcelTypeRules.


        :param dimension_rules: The dimension_rules of this ParcelTypeRules.  # noqa: E501
        :type: list[DimensionRules]
        """

        self._dimension_rules = dimension_rules

    @property
    def suggested_trackable_special_service_id(self):
        """Gets the suggested_trackable_special_service_id of this ParcelTypeRules.  # noqa: E501


        :return: The suggested_trackable_special_service_id of this ParcelTypeRules.  # noqa: E501
        :rtype: SpecialServiceCodes
        """
        return self._suggested_trackable_special_service_id

    @suggested_trackable_special_service_id.setter
    def suggested_trackable_special_service_id(self, suggested_trackable_special_service_id):
        """Sets the suggested_trackable_special_service_id of this ParcelTypeRules.


        :param suggested_trackable_special_service_id: The suggested_trackable_special_service_id of this ParcelTypeRules.  # noqa: E501
        :type: SpecialServiceCodes
        """

        self._suggested_trackable_special_service_id = suggested_trackable_special_service_id

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
        if not isinstance(other, ParcelTypeRules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelTypeRules):
            return True

        return self.to_dict() != other.to_dict()
