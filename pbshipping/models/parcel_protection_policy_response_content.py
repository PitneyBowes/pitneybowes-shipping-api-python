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


class ParcelProtectionPolicyResponseContent(object):
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
        'transaction_id': 'str',
        'developer_id': 'str',
        'subscription_acc_no': 'str',
        'client_transaction_id': 'str',
        'policy_details': 'ParcelProtectionPolicyResponsePolicyDetails',
        'shipment_details': 'ParcelProtectionPolicyResponseShipmentDetails',
        'shipper_info': 'ParcelProtectionPolicyResponseShipperInfo',
        'consignee_info': 'ParcelProtectionPolicyResponseShipperInfo',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'developer_id': 'developerId',
        'subscription_acc_no': 'subscriptionAccNo',
        'client_transaction_id': 'clientTransactionId',
        'policy_details': 'policyDetails',
        'shipment_details': 'shipmentDetails',
        'shipper_info': 'shipperInfo',
        'consignee_info': 'consigneeInfo',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, transaction_id=None, developer_id=None, subscription_acc_no=None, client_transaction_id=None, policy_details=None, shipment_details=None, shipper_info=None, consignee_info=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionPolicyResponseContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_id = None
        self._developer_id = None
        self._subscription_acc_no = None
        self._client_transaction_id = None
        self._policy_details = None
        self._shipment_details = None
        self._shipper_info = None
        self._consignee_info = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if transaction_id is not None:
            self.transaction_id = transaction_id
        if developer_id is not None:
            self.developer_id = developer_id
        if subscription_acc_no is not None:
            self.subscription_acc_no = subscription_acc_no
        if client_transaction_id is not None:
            self.client_transaction_id = client_transaction_id
        if policy_details is not None:
            self.policy_details = policy_details
        if shipment_details is not None:
            self.shipment_details = shipment_details
        if shipper_info is not None:
            self.shipper_info = shipper_info
        if consignee_info is not None:
            self.consignee_info = consignee_info
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ParcelProtectionPolicyResponseContent.


        :param transaction_id: The transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def developer_id(self):
        """Gets the developer_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The developer_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._developer_id

    @developer_id.setter
    def developer_id(self, developer_id):
        """Sets the developer_id of this ParcelProtectionPolicyResponseContent.


        :param developer_id: The developer_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._developer_id = developer_id

    @property
    def subscription_acc_no(self):
        """Gets the subscription_acc_no of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The subscription_acc_no of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._subscription_acc_no

    @subscription_acc_no.setter
    def subscription_acc_no(self, subscription_acc_no):
        """Sets the subscription_acc_no of this ParcelProtectionPolicyResponseContent.


        :param subscription_acc_no: The subscription_acc_no of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._subscription_acc_no = subscription_acc_no

    @property
    def client_transaction_id(self):
        """Gets the client_transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The client_transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._client_transaction_id

    @client_transaction_id.setter
    def client_transaction_id(self, client_transaction_id):
        """Sets the client_transaction_id of this ParcelProtectionPolicyResponseContent.


        :param client_transaction_id: The client_transaction_id of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._client_transaction_id = client_transaction_id

    @property
    def policy_details(self):
        """Gets the policy_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The policy_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: ParcelProtectionPolicyResponsePolicyDetails
        """
        return self._policy_details

    @policy_details.setter
    def policy_details(self, policy_details):
        """Sets the policy_details of this ParcelProtectionPolicyResponseContent.


        :param policy_details: The policy_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: ParcelProtectionPolicyResponsePolicyDetails
        """

        self._policy_details = policy_details

    @property
    def shipment_details(self):
        """Gets the shipment_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The shipment_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: ParcelProtectionPolicyResponseShipmentDetails
        """
        return self._shipment_details

    @shipment_details.setter
    def shipment_details(self, shipment_details):
        """Sets the shipment_details of this ParcelProtectionPolicyResponseContent.


        :param shipment_details: The shipment_details of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: ParcelProtectionPolicyResponseShipmentDetails
        """

        self._shipment_details = shipment_details

    @property
    def shipper_info(self):
        """Gets the shipper_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The shipper_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: ParcelProtectionPolicyResponseShipperInfo
        """
        return self._shipper_info

    @shipper_info.setter
    def shipper_info(self, shipper_info):
        """Sets the shipper_info of this ParcelProtectionPolicyResponseContent.


        :param shipper_info: The shipper_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: ParcelProtectionPolicyResponseShipperInfo
        """

        self._shipper_info = shipper_info

    @property
    def consignee_info(self):
        """Gets the consignee_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The consignee_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: ParcelProtectionPolicyResponseShipperInfo
        """
        return self._consignee_info

    @consignee_info.setter
    def consignee_info(self, consignee_info):
        """Sets the consignee_info of this ParcelProtectionPolicyResponseContent.


        :param consignee_info: The consignee_info of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: ParcelProtectionPolicyResponseShipperInfo
        """

        self._consignee_info = consignee_info

    @property
    def created_at(self):
        """Gets the created_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The created_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ParcelProtectionPolicyResponseContent.


        :param created_at: The created_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501


        :return: The updated_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ParcelProtectionPolicyResponseContent.


        :param updated_at: The updated_at of this ParcelProtectionPolicyResponseContent.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, ParcelProtectionPolicyResponseContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionPolicyResponseContent):
            return True

        return self.to_dict() != other.to_dict()
