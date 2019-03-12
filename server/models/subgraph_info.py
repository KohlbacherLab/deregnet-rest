# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from deregnet_rest.models.base_model_ import Model
from deregnet_rest import util


class SubgraphInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, run_id: str=None, num_nodes: int=None, num_edges: int=None, optimal: bool=None, optimality_type: str=None, root: str=None, score: float=None):  # noqa: E501
        """SubgraphInfo - a model defined in Swagger

        :param id: The id of this SubgraphInfo.  # noqa: E501
        :type id: str
        :param run_id: The run_id of this SubgraphInfo.  # noqa: E501
        :type run_id: str
        :param num_nodes: The num_nodes of this SubgraphInfo.  # noqa: E501
        :type num_nodes: int
        :param num_edges: The num_edges of this SubgraphInfo.  # noqa: E501
        :type num_edges: int
        :param optimal: The optimal of this SubgraphInfo.  # noqa: E501
        :type optimal: bool
        :param optimality_type: The optimality_type of this SubgraphInfo.  # noqa: E501
        :type optimality_type: str
        :param root: The root of this SubgraphInfo.  # noqa: E501
        :type root: str
        :param score: The score of this SubgraphInfo.  # noqa: E501
        :type score: float
        """
        self.swagger_types = {
            'id': str,
            'run_id': str,
            'num_nodes': int,
            'num_edges': int,
            'optimal': bool,
            'optimality_type': str,
            'root': str,
            'score': float
        }

        self.attribute_map = {
            'id': 'id',
            'run_id': 'run_id',
            'num_nodes': 'num_nodes',
            'num_edges': 'num_edges',
            'optimal': 'optimal',
            'optimality_type': 'optimality_type',
            'root': 'root',
            'score': 'score'
        }

        self._id = id
        self._run_id = run_id
        self._num_nodes = num_nodes
        self._num_edges = num_edges
        self._optimal = optimal
        self._optimality_type = optimality_type
        self._root = root
        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'SubgraphInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubgraphInfo of this SubgraphInfo.  # noqa: E501
        :rtype: SubgraphInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SubgraphInfo.

        Subgraph Id  # noqa: E501

        :return: The id of this SubgraphInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SubgraphInfo.

        Subgraph Id  # noqa: E501

        :param id: The id of this SubgraphInfo.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def run_id(self) -> str:
        """Gets the run_id of this SubgraphInfo.

        Id of run the subgraph is a result of  # noqa: E501

        :return: The run_id of this SubgraphInfo.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id: str):
        """Sets the run_id of this SubgraphInfo.

        Id of run the subgraph is a result of  # noqa: E501

        :param run_id: The run_id of this SubgraphInfo.
        :type run_id: str
        """
        if run_id is None:
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def num_nodes(self) -> int:
        """Gets the num_nodes of this SubgraphInfo.

        Number of nodes in subgraph  # noqa: E501

        :return: The num_nodes of this SubgraphInfo.
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes: int):
        """Sets the num_nodes of this SubgraphInfo.

        Number of nodes in subgraph  # noqa: E501

        :param num_nodes: The num_nodes of this SubgraphInfo.
        :type num_nodes: int
        """
        if num_nodes is None:
            raise ValueError("Invalid value for `num_nodes`, must not be `None`")  # noqa: E501

        self._num_nodes = num_nodes

    @property
    def num_edges(self) -> int:
        """Gets the num_edges of this SubgraphInfo.

        Number of edges in subgraph  # noqa: E501

        :return: The num_edges of this SubgraphInfo.
        :rtype: int
        """
        return self._num_edges

    @num_edges.setter
    def num_edges(self, num_edges: int):
        """Sets the num_edges of this SubgraphInfo.

        Number of edges in subgraph  # noqa: E501

        :param num_edges: The num_edges of this SubgraphInfo.
        :type num_edges: int
        """
        if num_edges is None:
            raise ValueError("Invalid value for `num_edges`, must not be `None`")  # noqa: E501

        self._num_edges = num_edges

    @property
    def optimal(self) -> bool:
        """Gets the optimal of this SubgraphInfo.

        Whether the subgraph is optimal, ie not prematurely stopped by a 'gap_cut' or 'time_limit'. This field is independent from the 'optimality_type' field.   # noqa: E501

        :return: The optimal of this SubgraphInfo.
        :rtype: bool
        """
        return self._optimal

    @optimal.setter
    def optimal(self, optimal: bool):
        """Sets the optimal of this SubgraphInfo.

        Whether the subgraph is optimal, ie not prematurely stopped by a 'gap_cut' or 'time_limit'. This field is independent from the 'optimality_type' field.   # noqa: E501

        :param optimal: The optimal of this SubgraphInfo.
        :type optimal: bool
        """
        if optimal is None:
            raise ValueError("Invalid value for `optimal`, must not be `None`")  # noqa: E501

        self._optimal = optimal

    @property
    def optimality_type(self) -> str:
        """Gets the optimality_type of this SubgraphInfo.

        'optimal': optimal subgraph 'suboptimal:1': first suboptimal subgraph 'suboptimal:2': second suboptimal subgraph, etc. ...   # noqa: E501

        :return: The optimality_type of this SubgraphInfo.
        :rtype: str
        """
        return self._optimality_type

    @optimality_type.setter
    def optimality_type(self, optimality_type: str):
        """Sets the optimality_type of this SubgraphInfo.

        'optimal': optimal subgraph 'suboptimal:1': first suboptimal subgraph 'suboptimal:2': second suboptimal subgraph, etc. ...   # noqa: E501

        :param optimality_type: The optimality_type of this SubgraphInfo.
        :type optimality_type: str
        """
        if optimality_type is None:
            raise ValueError("Invalid value for `optimality_type`, must not be `None`")  # noqa: E501

        self._optimality_type = optimality_type

    @property
    def root(self) -> str:
        """Gets the root of this SubgraphInfo.

        Id of root node, either predefined or found by algorithm   # noqa: E501

        :return: The root of this SubgraphInfo.
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root: str):
        """Sets the root of this SubgraphInfo.

        Id of root node, either predefined or found by algorithm   # noqa: E501

        :param root: The root of this SubgraphInfo.
        :type root: str
        """
        if root is None:
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def score(self) -> float:
        """Gets the score of this SubgraphInfo.

        Score of the subgraph  # noqa: E501

        :return: The score of this SubgraphInfo.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this SubgraphInfo.

        Score of the subgraph  # noqa: E501

        :param score: The score of this SubgraphInfo.
        :type score: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score