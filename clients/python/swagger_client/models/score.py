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


class Score(object):
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
        'description': 'str',
        'node_ids': 'list[str]',
        'score_values': 'list[float]'
    }

    attribute_map = {
        'description': 'description',
        'node_ids': 'node_ids',
        'score_values': 'score_values'
    }

    def __init__(self, description=None, node_ids=None, score_values=None):  # noqa: E501
        """Score - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._node_ids = None
        self._score_values = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if node_ids is not None:
            self.node_ids = node_ids
        if score_values is not None:
            self.score_values = score_values

    @property
    def description(self):
        """Gets the description of this Score.  # noqa: E501

        Description of the score  # noqa: E501

        :return: The description of this Score.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Score.

        Description of the score  # noqa: E501

        :param description: The description of this Score.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def node_ids(self):
        """Gets the node_ids of this Score.  # noqa: E501


        :return: The node_ids of this Score.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this Score.


        :param node_ids: The node_ids of this Score.  # noqa: E501
        :type: list[str]
        """

        self._node_ids = node_ids

    @property
    def score_values(self):
        """Gets the score_values of this Score.  # noqa: E501


        :return: The score_values of this Score.  # noqa: E501
        :rtype: list[float]
        """
        return self._score_values

    @score_values.setter
    def score_values(self, score_values):
        """Sets the score_values of this Score.


        :param score_values: The score_values of this Score.  # noqa: E501
        :type: list[float]
        """

        self._score_values = score_values

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
        if not isinstance(other, Score):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
