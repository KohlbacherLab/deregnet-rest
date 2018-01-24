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


class GraphInfo(object):
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
        'name': 'str',
        'description': 'str',
        'num_nodes': 'int',
        'num_edges': 'int',
        'id': 'str',
        'time_of_upload': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'num_nodes': 'num_nodes',
        'num_edges': 'num_edges',
        'id': 'id',
        'time_of_upload': 'time_of_upload'
    }

    def __init__(self, name=None, description=None, num_nodes=None, num_edges=None, id=None, time_of_upload=None):  # noqa: E501
        """GraphInfo - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._num_nodes = None
        self._num_edges = None
        self._id = None
        self._time_of_upload = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.id = id
        self.time_of_upload = time_of_upload

    @property
    def name(self):
        """Gets the name of this GraphInfo.  # noqa: E501

        Name of the graph  # noqa: E501

        :return: The name of this GraphInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GraphInfo.

        Name of the graph  # noqa: E501

        :param name: The name of this GraphInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GraphInfo.  # noqa: E501

        Description of the graph  # noqa: E501

        :return: The description of this GraphInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GraphInfo.

        Description of the graph  # noqa: E501

        :param description: The description of this GraphInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def num_nodes(self):
        """Gets the num_nodes of this GraphInfo.  # noqa: E501

        Number of nodes in the graph  # noqa: E501

        :return: The num_nodes of this GraphInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes):
        """Sets the num_nodes of this GraphInfo.

        Number of nodes in the graph  # noqa: E501

        :param num_nodes: The num_nodes of this GraphInfo.  # noqa: E501
        :type: int
        """
        if num_nodes is None:
            raise ValueError("Invalid value for `num_nodes`, must not be `None`")  # noqa: E501

        self._num_nodes = num_nodes

    @property
    def num_edges(self):
        """Gets the num_edges of this GraphInfo.  # noqa: E501

        Number of edges in the graph  # noqa: E501

        :return: The num_edges of this GraphInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_edges

    @num_edges.setter
    def num_edges(self, num_edges):
        """Sets the num_edges of this GraphInfo.

        Number of edges in the graph  # noqa: E501

        :param num_edges: The num_edges of this GraphInfo.  # noqa: E501
        :type: int
        """
        if num_edges is None:
            raise ValueError("Invalid value for `num_edges`, must not be `None`")  # noqa: E501

        self._num_edges = num_edges

    @property
    def id(self):
        """Gets the id of this GraphInfo.  # noqa: E501

        Id of the graph  # noqa: E501

        :return: The id of this GraphInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GraphInfo.

        Id of the graph  # noqa: E501

        :param id: The id of this GraphInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def time_of_upload(self):
        """Gets the time_of_upload of this GraphInfo.  # noqa: E501

        Time of upload  # noqa: E501

        :return: The time_of_upload of this GraphInfo.  # noqa: E501
        :rtype: str
        """
        return self._time_of_upload

    @time_of_upload.setter
    def time_of_upload(self, time_of_upload):
        """Sets the time_of_upload of this GraphInfo.

        Time of upload  # noqa: E501

        :param time_of_upload: The time_of_upload of this GraphInfo.  # noqa: E501
        :type: str
        """
        if time_of_upload is None:
            raise ValueError("Invalid value for `time_of_upload`, must not be `None`")  # noqa: E501

        self._time_of_upload = time_of_upload

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
        if not isinstance(other, GraphInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other