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


class GroupInfo(object):
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
        'id': 'int',
        'name': 'str',
        'workspace_id': 'int',
        'drm_enabled': 'bool',
        'drm_expires_after': 'str',
        'expire_workspace_access': 'str',
        'expire_workspace_access_at': 'str',
        'watermarked': 'bool',
        'file_managing_abilities': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'drm_enabled': 'drm_enabled',
        'drm_expires_after': 'drm_expires_after',
        'expire_workspace_access': 'expire_workspace_access',
        'expire_workspace_access_at': 'expire_workspace_access_at',
        'watermarked': 'watermarked',
        'file_managing_abilities': 'file_managing_abilities'
    }

    def __init__(self, id=None, name=None, workspace_id=None, drm_enabled=None, drm_expires_after=None, expire_workspace_access=None, expire_workspace_access_at=None, watermarked=None, file_managing_abilities=None):
        """
        GroupInfo - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._workspace_id = None
        self._drm_enabled = None
        self._drm_expires_after = None
        self._expire_workspace_access = None
        self._expire_workspace_access_at = None
        self._watermarked = None
        self._file_managing_abilities = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if workspace_id is not None:
          self.workspace_id = workspace_id
        if drm_enabled is not None:
          self.drm_enabled = drm_enabled
        if drm_expires_after is not None:
          self.drm_expires_after = drm_expires_after
        if expire_workspace_access is not None:
          self.expire_workspace_access = expire_workspace_access
        if expire_workspace_access_at is not None:
          self.expire_workspace_access_at = expire_workspace_access_at
        if watermarked is not None:
          self.watermarked = watermarked
        if file_managing_abilities is not None:
          self.file_managing_abilities = file_managing_abilities

    @property
    def id(self):
        """
        Gets the id of this GroupInfo.

        :return: The id of this GroupInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupInfo.

        :param id: The id of this GroupInfo.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GroupInfo.

        :return: The name of this GroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupInfo.

        :param name: The name of this GroupInfo.
        :type: str
        """

        self._name = name

    @property
    def workspace_id(self):
        """
        Gets the workspace_id of this GroupInfo.

        :return: The workspace_id of this GroupInfo.
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this GroupInfo.

        :param workspace_id: The workspace_id of this GroupInfo.
        :type: int
        """

        self._workspace_id = workspace_id

    @property
    def drm_enabled(self):
        """
        Gets the drm_enabled of this GroupInfo.

        :return: The drm_enabled of this GroupInfo.
        :rtype: bool
        """
        return self._drm_enabled

    @drm_enabled.setter
    def drm_enabled(self, drm_enabled):
        """
        Sets the drm_enabled of this GroupInfo.

        :param drm_enabled: The drm_enabled of this GroupInfo.
        :type: bool
        """

        self._drm_enabled = drm_enabled

    @property
    def drm_expires_after(self):
        """
        Gets the drm_expires_after of this GroupInfo.

        :return: The drm_expires_after of this GroupInfo.
        :rtype: str
        """
        return self._drm_expires_after

    @drm_expires_after.setter
    def drm_expires_after(self, drm_expires_after):
        """
        Sets the drm_expires_after of this GroupInfo.

        :param drm_expires_after: The drm_expires_after of this GroupInfo.
        :type: str
        """

        self._drm_expires_after = drm_expires_after

    @property
    def expire_workspace_access(self):
        """
        Gets the expire_workspace_access of this GroupInfo.

        :return: The expire_workspace_access of this GroupInfo.
        :rtype: str
        """
        return self._expire_workspace_access

    @expire_workspace_access.setter
    def expire_workspace_access(self, expire_workspace_access):
        """
        Sets the expire_workspace_access of this GroupInfo.

        :param expire_workspace_access: The expire_workspace_access of this GroupInfo.
        :type: str
        """

        self._expire_workspace_access = expire_workspace_access

    @property
    def expire_workspace_access_at(self):
        """
        Gets the expire_workspace_access_at of this GroupInfo.

        :return: The expire_workspace_access_at of this GroupInfo.
        :rtype: str
        """
        return self._expire_workspace_access_at

    @expire_workspace_access_at.setter
    def expire_workspace_access_at(self, expire_workspace_access_at):
        """
        Sets the expire_workspace_access_at of this GroupInfo.

        :param expire_workspace_access_at: The expire_workspace_access_at of this GroupInfo.
        :type: str
        """

        self._expire_workspace_access_at = expire_workspace_access_at

    @property
    def watermarked(self):
        """
        Gets the watermarked of this GroupInfo.

        :return: The watermarked of this GroupInfo.
        :rtype: bool
        """
        return self._watermarked

    @watermarked.setter
    def watermarked(self, watermarked):
        """
        Sets the watermarked of this GroupInfo.

        :param watermarked: The watermarked of this GroupInfo.
        :type: bool
        """

        self._watermarked = watermarked

    @property
    def file_managing_abilities(self):
        """
        Gets the file_managing_abilities of this GroupInfo.

        :return: The file_managing_abilities of this GroupInfo.
        :rtype: bool
        """
        return self._file_managing_abilities

    @file_managing_abilities.setter
    def file_managing_abilities(self, file_managing_abilities):
        """
        Sets the file_managing_abilities of this GroupInfo.

        :param file_managing_abilities: The file_managing_abilities of this GroupInfo.
        :type: bool
        """

        self._file_managing_abilities = file_managing_abilities

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
        if not isinstance(other, GroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
