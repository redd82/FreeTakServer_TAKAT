# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RemoteSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, filter_groups: List[str]=None, notes: str=None, callsign: str=None, team: str=None, role: str=None, takv: str=None, uid: str=None):  # noqa: E501
        """RemoteSubscription - a model defined in Swagger

        :param filter_groups: The filter_groups of this RemoteSubscription.  # noqa: E501
        :type filter_groups: List[str]
        :param notes: The notes of this RemoteSubscription.  # noqa: E501
        :type notes: str
        :param callsign: The callsign of this RemoteSubscription.  # noqa: E501
        :type callsign: str
        :param team: The team of this RemoteSubscription.  # noqa: E501
        :type team: str
        :param role: The role of this RemoteSubscription.  # noqa: E501
        :type role: str
        :param takv: The takv of this RemoteSubscription.  # noqa: E501
        :type takv: str
        :param uid: The uid of this RemoteSubscription.  # noqa: E501
        :type uid: str
        """
        self.swagger_types = {
            'filter_groups': List[str],
            'notes': str,
            'callsign': str,
            'team': str,
            'role': str,
            'takv': str,
            'uid': str
        }

        self.attribute_map = {
            'filter_groups': 'filterGroups',
            'notes': 'notes',
            'callsign': 'callsign',
            'team': 'team',
            'role': 'role',
            'takv': 'takv',
            'uid': 'uid'
        }
        self._filter_groups = filter_groups
        self._notes = notes
        self._callsign = callsign
        self._team = team
        self._role = role
        self._takv = takv
        self._uid = uid

    @classmethod
    def from_dict(cls, dikt) -> 'RemoteSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RemoteSubscription of this RemoteSubscription.  # noqa: E501
        :rtype: RemoteSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filter_groups(self) -> List[str]:
        """Gets the filter_groups of this RemoteSubscription.


        :return: The filter_groups of this RemoteSubscription.
        :rtype: List[str]
        """
        return self._filter_groups

    @filter_groups.setter
    def filter_groups(self, filter_groups: List[str]):
        """Sets the filter_groups of this RemoteSubscription.


        :param filter_groups: The filter_groups of this RemoteSubscription.
        :type filter_groups: List[str]
        """

        self._filter_groups = filter_groups

    @property
    def notes(self) -> str:
        """Gets the notes of this RemoteSubscription.


        :return: The notes of this RemoteSubscription.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this RemoteSubscription.


        :param notes: The notes of this RemoteSubscription.
        :type notes: str
        """

        self._notes = notes

    @property
    def callsign(self) -> str:
        """Gets the callsign of this RemoteSubscription.


        :return: The callsign of this RemoteSubscription.
        :rtype: str
        """
        return self._callsign

    @callsign.setter
    def callsign(self, callsign: str):
        """Sets the callsign of this RemoteSubscription.


        :param callsign: The callsign of this RemoteSubscription.
        :type callsign: str
        """

        self._callsign = callsign

    @property
    def team(self) -> str:
        """Gets the team of this RemoteSubscription.


        :return: The team of this RemoteSubscription.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team: str):
        """Sets the team of this RemoteSubscription.


        :param team: The team of this RemoteSubscription.
        :type team: str
        """

        self._team = team

    @property
    def role(self) -> str:
        """Gets the role of this RemoteSubscription.


        :return: The role of this RemoteSubscription.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this RemoteSubscription.


        :param role: The role of this RemoteSubscription.
        :type role: str
        """

        self._role = role

    @property
    def takv(self) -> str:
        """Gets the takv of this RemoteSubscription.


        :return: The takv of this RemoteSubscription.
        :rtype: str
        """
        return self._takv

    @takv.setter
    def takv(self, takv: str):
        """Sets the takv of this RemoteSubscription.


        :param takv: The takv of this RemoteSubscription.
        :type takv: str
        """

        self._takv = takv

    @property
    def uid(self) -> str:
        """Gets the uid of this RemoteSubscription.


        :return: The uid of this RemoteSubscription.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        """Sets the uid of this RemoteSubscription.


        :param uid: The uid of this RemoteSubscription.
        :type uid: str
        """

        self._uid = uid