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


class ParcelProtectionPolicyResponseShipperInfo(object):
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
        'shipper_id': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'email': 'str',
        'phone_number1': 'str',
        'phone_number2': 'str',
        'fax_number': 'str',
        'address': 'ParcelProtectionPolicyResponseShipperInfoAddress'
    }

    attribute_map = {
        'shipper_id': 'shipperID',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'company': 'company',
        'email': 'email',
        'phone_number1': 'phoneNumber1',
        'phone_number2': 'phoneNumber2',
        'fax_number': 'faxNumber',
        'address': 'address'
    }

    def __init__(self, shipper_id=None, first_name=None, middle_name=None, last_name=None, company=None, email=None, phone_number1=None, phone_number2=None, fax_number=None, address=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionPolicyResponseShipperInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._shipper_id = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._company = None
        self._email = None
        self._phone_number1 = None
        self._phone_number2 = None
        self._fax_number = None
        self._address = None
        self.discriminator = None

        if shipper_id is not None:
            self.shipper_id = shipper_id
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if company is not None:
            self.company = company
        if email is not None:
            self.email = email
        if phone_number1 is not None:
            self.phone_number1 = phone_number1
        if phone_number2 is not None:
            self.phone_number2 = phone_number2
        if fax_number is not None:
            self.fax_number = fax_number
        if address is not None:
            self.address = address

    @property
    def shipper_id(self):
        """Gets the shipper_id of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The shipper_id of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._shipper_id

    @shipper_id.setter
    def shipper_id(self, shipper_id):
        """Sets the shipper_id of this ParcelProtectionPolicyResponseShipperInfo.


        :param shipper_id: The shipper_id of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._shipper_id = shipper_id

    @property
    def first_name(self):
        """Gets the first_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The first_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ParcelProtectionPolicyResponseShipperInfo.


        :param first_name: The first_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The middle_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ParcelProtectionPolicyResponseShipperInfo.


        :param middle_name: The middle_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The last_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ParcelProtectionPolicyResponseShipperInfo.


        :param last_name: The last_name of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The company of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ParcelProtectionPolicyResponseShipperInfo.


        :param company: The company of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def email(self):
        """Gets the email of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The email of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParcelProtectionPolicyResponseShipperInfo.


        :param email: The email of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number1(self):
        """Gets the phone_number1 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The phone_number1 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone_number1

    @phone_number1.setter
    def phone_number1(self, phone_number1):
        """Sets the phone_number1 of this ParcelProtectionPolicyResponseShipperInfo.


        :param phone_number1: The phone_number1 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._phone_number1 = phone_number1

    @property
    def phone_number2(self):
        """Gets the phone_number2 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The phone_number2 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone_number2

    @phone_number2.setter
    def phone_number2(self, phone_number2):
        """Sets the phone_number2 of this ParcelProtectionPolicyResponseShipperInfo.


        :param phone_number2: The phone_number2 of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._phone_number2 = phone_number2

    @property
    def fax_number(self):
        """Gets the fax_number of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The fax_number of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this ParcelProtectionPolicyResponseShipperInfo.


        :param fax_number: The fax_number of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: str
        """

        self._fax_number = fax_number

    @property
    def address(self):
        """Gets the address of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501


        :return: The address of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :rtype: ParcelProtectionPolicyResponseShipperInfoAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ParcelProtectionPolicyResponseShipperInfo.


        :param address: The address of this ParcelProtectionPolicyResponseShipperInfo.  # noqa: E501
        :type: ParcelProtectionPolicyResponseShipperInfoAddress
        """

        self._address = address

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
        if not isinstance(other, ParcelProtectionPolicyResponseShipperInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionPolicyResponseShipperInfo):
            return True

        return self.to_dict() != other.to_dict()