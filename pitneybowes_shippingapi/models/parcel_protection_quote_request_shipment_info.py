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


class ParcelProtectionQuoteRequestShipmentInfo(object):
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
        'carrier': 'str',
        'service_id': 'str',
        'insurance_coverage_value': 'int',
        'insurance_coverage_value_currency': 'str',
        'parcel_info': 'ParcelProtectionQuoteRequestShipmentInfoParcelInfo',
        'shipper_info': 'ParcelProtectionQuoteRequestShipmentInfoShipperInfo',
        'consignee_info': 'ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo'
    }

    attribute_map = {
        'carrier': 'carrier',
        'service_id': 'serviceId',
        'insurance_coverage_value': 'insuranceCoverageValue',
        'insurance_coverage_value_currency': 'insuranceCoverageValueCurrency',
        'parcel_info': 'parcelInfo',
        'shipper_info': 'shipperInfo',
        'consignee_info': 'consigneeInfo'
    }

    def __init__(self, carrier=None, service_id=None, insurance_coverage_value=None, insurance_coverage_value_currency=None, parcel_info=None, shipper_info=None, consignee_info=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionQuoteRequestShipmentInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._carrier = None
        self._service_id = None
        self._insurance_coverage_value = None
        self._insurance_coverage_value_currency = None
        self._parcel_info = None
        self._shipper_info = None
        self._consignee_info = None
        self.discriminator = None

        self.carrier = carrier
        self.service_id = service_id
        self.insurance_coverage_value = insurance_coverage_value
        self.insurance_coverage_value_currency = insurance_coverage_value_currency
        self.parcel_info = parcel_info
        self.shipper_info = shipper_info
        self.consignee_info = consignee_info

    @property
    def carrier(self):
        """Gets the carrier of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The carrier of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this ParcelProtectionQuoteRequestShipmentInfo.


        :param carrier: The carrier of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and carrier is None:  # noqa: E501
            raise ValueError("Invalid value for `carrier`, must not be `None`")  # noqa: E501

        self._carrier = carrier

    @property
    def service_id(self):
        """Gets the service_id of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The service_id of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ParcelProtectionQuoteRequestShipmentInfo.


        :param service_id: The service_id of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_id is None:  # noqa: E501
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def insurance_coverage_value(self):
        """Gets the insurance_coverage_value of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The insurance_coverage_value of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: int
        """
        return self._insurance_coverage_value

    @insurance_coverage_value.setter
    def insurance_coverage_value(self, insurance_coverage_value):
        """Sets the insurance_coverage_value of this ParcelProtectionQuoteRequestShipmentInfo.


        :param insurance_coverage_value: The insurance_coverage_value of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and insurance_coverage_value is None:  # noqa: E501
            raise ValueError("Invalid value for `insurance_coverage_value`, must not be `None`")  # noqa: E501

        self._insurance_coverage_value = insurance_coverage_value

    @property
    def insurance_coverage_value_currency(self):
        """Gets the insurance_coverage_value_currency of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The insurance_coverage_value_currency of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: str
        """
        return self._insurance_coverage_value_currency

    @insurance_coverage_value_currency.setter
    def insurance_coverage_value_currency(self, insurance_coverage_value_currency):
        """Sets the insurance_coverage_value_currency of this ParcelProtectionQuoteRequestShipmentInfo.


        :param insurance_coverage_value_currency: The insurance_coverage_value_currency of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and insurance_coverage_value_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `insurance_coverage_value_currency`, must not be `None`")  # noqa: E501

        self._insurance_coverage_value_currency = insurance_coverage_value_currency

    @property
    def parcel_info(self):
        """Gets the parcel_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The parcel_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: ParcelProtectionQuoteRequestShipmentInfoParcelInfo
        """
        return self._parcel_info

    @parcel_info.setter
    def parcel_info(self, parcel_info):
        """Sets the parcel_info of this ParcelProtectionQuoteRequestShipmentInfo.


        :param parcel_info: The parcel_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: ParcelProtectionQuoteRequestShipmentInfoParcelInfo
        """
        if self.local_vars_configuration.client_side_validation and parcel_info is None:  # noqa: E501
            raise ValueError("Invalid value for `parcel_info`, must not be `None`")  # noqa: E501

        self._parcel_info = parcel_info

    @property
    def shipper_info(self):
        """Gets the shipper_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The shipper_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: ParcelProtectionQuoteRequestShipmentInfoShipperInfo
        """
        return self._shipper_info

    @shipper_info.setter
    def shipper_info(self, shipper_info):
        """Sets the shipper_info of this ParcelProtectionQuoteRequestShipmentInfo.


        :param shipper_info: The shipper_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: ParcelProtectionQuoteRequestShipmentInfoShipperInfo
        """
        if self.local_vars_configuration.client_side_validation and shipper_info is None:  # noqa: E501
            raise ValueError("Invalid value for `shipper_info`, must not be `None`")  # noqa: E501

        self._shipper_info = shipper_info

    @property
    def consignee_info(self):
        """Gets the consignee_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501


        :return: The consignee_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :rtype: ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo
        """
        return self._consignee_info

    @consignee_info.setter
    def consignee_info(self, consignee_info):
        """Sets the consignee_info of this ParcelProtectionQuoteRequestShipmentInfo.


        :param consignee_info: The consignee_info of this ParcelProtectionQuoteRequestShipmentInfo.  # noqa: E501
        :type: ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo
        """
        if self.local_vars_configuration.client_side_validation and consignee_info is None:  # noqa: E501
            raise ValueError("Invalid value for `consignee_info`, must not be `None`")  # noqa: E501

        self._consignee_info = consignee_info

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
        if not isinstance(other, ParcelProtectionQuoteRequestShipmentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionQuoteRequestShipmentInfo):
            return True

        return self.to_dict() != other.to_dict()