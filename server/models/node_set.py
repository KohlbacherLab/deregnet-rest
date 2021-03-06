# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from deregnet_rest.models.base_model_ import Model
from deregnet_rest import util


class NodeSet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, nodes: List[str]=None):  # noqa: E501
        """NodeSet - a model defined in Swagger

        :param description: The description of this NodeSet.  # noqa: E501
        :type description: str
        :param nodes: The nodes of this NodeSet.  # noqa: E501
        :type nodes: List[str]
        """
        self.swagger_types = {
            'description': str,
            'nodes': List[str]
        }

        self.attribute_map = {
            'description': 'description',
            'nodes': 'nodes'
        }

        self._description = description
        self._nodes = nodes

    @classmethod
    def from_dict(cls, dikt) -> 'NodeSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodeSet of this NodeSet.  # noqa: E501
        :rtype: NodeSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this NodeSet.

        Description of the node set  # noqa: E501

        :return: The description of this NodeSet.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this NodeSet.

        Description of the node set  # noqa: E501

        :param description: The description of this NodeSet.
        :type description: str
        """

        self._description = description

    @property
    def nodes(self) -> List[str]:
        """Gets the nodes of this NodeSet.


        :return: The nodes of this NodeSet.
        :rtype: List[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: List[str]):
        """Sets the nodes of this NodeSet.


        :param nodes: The nodes of this NodeSet.
        :type nodes: List[str]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes
