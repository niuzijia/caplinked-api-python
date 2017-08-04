# coding: utf-8

"""
    CapLinked API v1.0

    Core information security endpoints for managing files/folders, users/groups, uploads/downloads, and more.

    OpenAPI spec version: 2017-05-23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExpiringUrl(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'expiring_url': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'expiring_url': 'expiring_url',
        'file_name': 'file_name'
    }

    def __init__(self, expiring_url=None, file_name=None):
        """
        ExpiringUrl - a model defined in Swagger
        """

        self._expiring_url = None
        self._file_name = None

        if expiring_url is not None:
          self.expiring_url = expiring_url
        if file_name is not None:
          self.file_name = file_name

    @property
    def expiring_url(self):
        """
        Gets the expiring_url of this ExpiringUrl.

        :return: The expiring_url of this ExpiringUrl.
        :rtype: str
        """
        return self._expiring_url

    @expiring_url.setter
    def expiring_url(self, expiring_url):
        """
        Sets the expiring_url of this ExpiringUrl.

        :param expiring_url: The expiring_url of this ExpiringUrl.
        :type: str
        """

        self._expiring_url = expiring_url

    @property
    def file_name(self):
        """
        Gets the file_name of this ExpiringUrl.

        :return: The file_name of this ExpiringUrl.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this ExpiringUrl.

        :param file_name: The file_name of this ExpiringUrl.
        :type: str
        """

        self._file_name = file_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ExpiringUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
