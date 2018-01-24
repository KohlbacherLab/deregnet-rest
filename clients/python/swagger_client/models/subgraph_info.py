# coding: utf-8

"""
    DeRegNet REST API

    DeRegNet REST API   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: deregnet@informatik.uni-tuebingen.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pprint
import re  # noqa: F401

import six


class SubgraphInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'num_nodes': 'int',
        'num_edges': 'int'
    }

    attribute_map = {
        'id': 'id',
        'num_nodes': 'num_nodes',
        'num_edges': 'num_edges'
    }

    def __init__(self, id=None, num_nodes=None, num_edges=None):  # noqa: E501
        """SubgraphInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._num_nodes = None
        self._num_edges = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if num_nodes is not None:
            self.num_nodes = num_nodes
        if num_edges is not None:
            self.num_edges = num_edges

    @property
    def id(self):
        """Gets the id of this SubgraphInfo.  # noqa: E501

        Subgraph Id  # noqa: E501

        :return: The id of this SubgraphInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubgraphInfo.

        Subgraph Id  # noqa: E501

        :param id: The id of this SubgraphInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def num_nodes(self):
        """Gets the num_nodes of this SubgraphInfo.  # noqa: E501

        Number of nodes in subgraph  # noqa: E501

        :return: The num_nodes of this SubgraphInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes):
        """Sets the num_nodes of this SubgraphInfo.

        Number of nodes in subgraph  # noqa: E501

        :param num_nodes: The num_nodes of this SubgraphInfo.  # noqa: E501
        :type: int
        """

        self._num_nodes = num_nodes

    @property
    def num_edges(self):
        """Gets the num_edges of this SubgraphInfo.  # noqa: E501

        Number of edges in subgraph  # noqa: E501

        :return: The num_edges of this SubgraphInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_edges

    @num_edges.setter
    def num_edges(self, num_edges):
        """Sets the num_edges of this SubgraphInfo.

        Number of edges in subgraph  # noqa: E501

        :param num_edges: The num_edges of this SubgraphInfo.  # noqa: E501
        :type: int
        """

        self._num_edges = num_edges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, SubgraphInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
