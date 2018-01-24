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


class RunInfo(object):
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
        'id': 'str',
        'post_time': 'str',
        'started': 'bool',
        'done': 'bool',
        'subgraph_ids': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'post_time': 'post_time',
        'started': 'started',
        'done': 'done',
        'subgraph_ids': 'subgraph_ids'
    }

    def __init__(self, description=None, id=None, post_time=None, started=None, done=None, subgraph_ids=None):  # noqa: E501
        """RunInfo - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._post_time = None
        self._started = None
        self._done = None
        self._subgraph_ids = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.id = id
        self.post_time = post_time
        self.started = started
        self.done = done
        if subgraph_ids is not None:
            self.subgraph_ids = subgraph_ids

    @property
    def description(self):
        """Gets the description of this RunInfo.  # noqa: E501

        Description of the run  # noqa: E501

        :return: The description of this RunInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunInfo.

        Description of the run  # noqa: E501

        :param description: The description of this RunInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this RunInfo.  # noqa: E501

        Id of the score object  # noqa: E501

        :return: The id of this RunInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RunInfo.

        Id of the score object  # noqa: E501

        :param id: The id of this RunInfo.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def post_time(self):
        """Gets the post_time of this RunInfo.  # noqa: E501

        Time of initial run post  # noqa: E501

        :return: The post_time of this RunInfo.  # noqa: E501
        :rtype: str
        """
        return self._post_time

    @post_time.setter
    def post_time(self, post_time):
        """Sets the post_time of this RunInfo.

        Time of initial run post  # noqa: E501

        :param post_time: The post_time of this RunInfo.  # noqa: E501
        :type: str
        """
        if post_time is None:
            raise ValueError("Invalid value for `post_time`, must not be `None`")  # noqa: E501

        self._post_time = post_time

    @property
    def started(self):
        """Gets the started of this RunInfo.  # noqa: E501

        Whether the run has already started  # noqa: E501

        :return: The started of this RunInfo.  # noqa: E501
        :rtype: bool
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this RunInfo.

        Whether the run has already started  # noqa: E501

        :param started: The started of this RunInfo.  # noqa: E501
        :type: bool
        """
        if started is None:
            raise ValueError("Invalid value for `started`, must not be `None`")  # noqa: E501

        self._started = started

    @property
    def done(self):
        """Gets the done of this RunInfo.  # noqa: E501

        Whether the run is completed  # noqa: E501

        :return: The done of this RunInfo.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this RunInfo.

        Whether the run is completed  # noqa: E501

        :param done: The done of this RunInfo.  # noqa: E501
        :type: bool
        """
        if done is None:
            raise ValueError("Invalid value for `done`, must not be `None`")  # noqa: E501

        self._done = done

    @property
    def subgraph_ids(self):
        """Gets the subgraph_ids of this RunInfo.  # noqa: E501


        :return: The subgraph_ids of this RunInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._subgraph_ids

    @subgraph_ids.setter
    def subgraph_ids(self, subgraph_ids):
        """Sets the subgraph_ids of this RunInfo.


        :param subgraph_ids: The subgraph_ids of this RunInfo.  # noqa: E501
        :type: list[str]
        """

        self._subgraph_ids = subgraph_ids

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
        if not isinstance(other, RunInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other