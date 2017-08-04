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


class Team(object):
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
        'team_owner_id': 'int',
        'creator_id': 'int',
        'allowed_workspaces': 'int',
        'allowed_admins': 'int',
        'drm_enabled': 'bool',
        'watermarking': 'bool',
        'suppress_emails': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'team_owner_id': 'team_owner_id',
        'creator_id': 'creator_id',
        'allowed_workspaces': 'allowed_workspaces',
        'allowed_admins': 'allowed_admins',
        'drm_enabled': 'drm_enabled',
        'watermarking': 'watermarking',
        'suppress_emails': 'suppress_emails'
    }

    def __init__(self, id=None, name=None, team_owner_id=None, creator_id=None, allowed_workspaces=None, allowed_admins=None, drm_enabled=None, watermarking=None, suppress_emails=None):
        """
        Team - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._team_owner_id = None
        self._creator_id = None
        self._allowed_workspaces = None
        self._allowed_admins = None
        self._drm_enabled = None
        self._watermarking = None
        self._suppress_emails = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if team_owner_id is not None:
          self.team_owner_id = team_owner_id
        if creator_id is not None:
          self.creator_id = creator_id
        if allowed_workspaces is not None:
          self.allowed_workspaces = allowed_workspaces
        if allowed_admins is not None:
          self.allowed_admins = allowed_admins
        if drm_enabled is not None:
          self.drm_enabled = drm_enabled
        if watermarking is not None:
          self.watermarking = watermarking
        if suppress_emails is not None:
          self.suppress_emails = suppress_emails

    @property
    def id(self):
        """
        Gets the id of this Team.

        :return: The id of this Team.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Team.

        :param id: The id of this Team.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Team.

        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Team.

        :param name: The name of this Team.
        :type: str
        """

        self._name = name

    @property
    def team_owner_id(self):
        """
        Gets the team_owner_id of this Team.

        :return: The team_owner_id of this Team.
        :rtype: int
        """
        return self._team_owner_id

    @team_owner_id.setter
    def team_owner_id(self, team_owner_id):
        """
        Sets the team_owner_id of this Team.

        :param team_owner_id: The team_owner_id of this Team.
        :type: int
        """

        self._team_owner_id = team_owner_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this Team.

        :return: The creator_id of this Team.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this Team.

        :param creator_id: The creator_id of this Team.
        :type: int
        """

        self._creator_id = creator_id

    @property
    def allowed_workspaces(self):
        """
        Gets the allowed_workspaces of this Team.

        :return: The allowed_workspaces of this Team.
        :rtype: int
        """
        return self._allowed_workspaces

    @allowed_workspaces.setter
    def allowed_workspaces(self, allowed_workspaces):
        """
        Sets the allowed_workspaces of this Team.

        :param allowed_workspaces: The allowed_workspaces of this Team.
        :type: int
        """

        self._allowed_workspaces = allowed_workspaces

    @property
    def allowed_admins(self):
        """
        Gets the allowed_admins of this Team.

        :return: The allowed_admins of this Team.
        :rtype: int
        """
        return self._allowed_admins

    @allowed_admins.setter
    def allowed_admins(self, allowed_admins):
        """
        Sets the allowed_admins of this Team.

        :param allowed_admins: The allowed_admins of this Team.
        :type: int
        """

        self._allowed_admins = allowed_admins

    @property
    def drm_enabled(self):
        """
        Gets the drm_enabled of this Team.

        :return: The drm_enabled of this Team.
        :rtype: bool
        """
        return self._drm_enabled

    @drm_enabled.setter
    def drm_enabled(self, drm_enabled):
        """
        Sets the drm_enabled of this Team.

        :param drm_enabled: The drm_enabled of this Team.
        :type: bool
        """

        self._drm_enabled = drm_enabled

    @property
    def watermarking(self):
        """
        Gets the watermarking of this Team.

        :return: The watermarking of this Team.
        :rtype: bool
        """
        return self._watermarking

    @watermarking.setter
    def watermarking(self, watermarking):
        """
        Sets the watermarking of this Team.

        :param watermarking: The watermarking of this Team.
        :type: bool
        """

        self._watermarking = watermarking

    @property
    def suppress_emails(self):
        """
        Gets the suppress_emails of this Team.

        :return: The suppress_emails of this Team.
        :rtype: bool
        """
        return self._suppress_emails

    @suppress_emails.setter
    def suppress_emails(self, suppress_emails):
        """
        Sets the suppress_emails of this Team.

        :param suppress_emails: The suppress_emails of this Team.
        :type: bool
        """

        self._suppress_emails = suppress_emails

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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other