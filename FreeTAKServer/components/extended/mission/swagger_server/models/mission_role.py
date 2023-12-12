# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MissionRole(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, permissions: List[str]=None, type: str=None):  # noqa: E501
        """MissionRole - a model defined in Swagger

        :param permissions: The permissions of this MissionRole.  # noqa: E501
        :type permissions: List[str]
        :param type: The type of this MissionRole.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'permissions': List[str],
            'type': str
        }

        self.attribute_map = {
            'permissions': 'permissions',
            'type': 'type'
        }
        self._permissions = permissions
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'MissionRole':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MissionRole of this MissionRole.  # noqa: E501
        :rtype: MissionRole
        """
        return util.deserialize_model(dikt, cls)

    @property
    def permissions(self) -> List[str]:
        """Gets the permissions of this MissionRole.


        :return: The permissions of this MissionRole.
        :rtype: List[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions: List[str]):
        """Sets the permissions of this MissionRole.


        :param permissions: The permissions of this MissionRole.
        :type permissions: List[str]
        """

        self._permissions = permissions

    @property
    def type(self) -> str:
        """Gets the type of this MissionRole.


        :return: The type of this MissionRole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MissionRole.


        :param type: The type of this MissionRole.
        :type type: str
        """
        allowed_values = ["MISSION_OWNER", "MISSION_SUBSCRIBER", "MISSION_READONLY_SUBSCRIBER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type