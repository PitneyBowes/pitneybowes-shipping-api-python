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


class InfectiousSubstanceContact(object):
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
        'company_name': 'str',
        'contact_id': 'str',
        'email_address': 'str',
        'person_name': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'contact_id': 'contactId',
        'email_address': 'emailAddress',
        'person_name': 'personName',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, company_name=None, contact_id=None, email_address=None, person_name=None, phone_number=None, local_vars_configuration=None):  # noqa: E501
        """InfectiousSubstanceContact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company_name = None
        self._contact_id = None
        self._email_address = None
        self._person_name = None
        self._phone_number = None
        self.discriminator = None

        if company_name is not None:
            self.company_name = company_name
        if contact_id is not None:
            self.contact_id = contact_id
        if email_address is not None:
            self.email_address = email_address
        if person_name is not None:
            self.person_name = person_name
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def company_name(self):
        """Gets the company_name of this InfectiousSubstanceContact.  # noqa: E501


        :return: The company_name of this InfectiousSubstanceContact.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this InfectiousSubstanceContact.


        :param company_name: The company_name of this InfectiousSubstanceContact.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def contact_id(self):
        """Gets the contact_id of this InfectiousSubstanceContact.  # noqa: E501


        :return: The contact_id of this InfectiousSubstanceContact.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this InfectiousSubstanceContact.


        :param contact_id: The contact_id of this InfectiousSubstanceContact.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def email_address(self):
        """Gets the email_address of this InfectiousSubstanceContact.  # noqa: E501


        :return: The email_address of this InfectiousSubstanceContact.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this InfectiousSubstanceContact.


        :param email_address: The email_address of this InfectiousSubstanceContact.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def person_name(self):
        """Gets the person_name of this InfectiousSubstanceContact.  # noqa: E501


        :return: The person_name of this InfectiousSubstanceContact.  # noqa: E501
        :rtype: str
        """
        return self._person_name

    @person_name.setter
    def person_name(self, person_name):
        """Sets the person_name of this InfectiousSubstanceContact.


        :param person_name: The person_name of this InfectiousSubstanceContact.  # noqa: E501
        :type: str
        """

        self._person_name = person_name

    @property
    def phone_number(self):
        """Gets the phone_number of this InfectiousSubstanceContact.  # noqa: E501


        :return: The phone_number of this InfectiousSubstanceContact.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this InfectiousSubstanceContact.


        :param phone_number: The phone_number of this InfectiousSubstanceContact.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if not isinstance(other, InfectiousSubstanceContact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfectiousSubstanceContact):
            return True

        return self.to_dict() != other.to_dict()
