# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from deregnet_rest.models.score import Score  # noqa: E501
from deregnet_rest.models.score_info import ScoreInfo  # noqa: E501
from deregnet_rest.test import BaseTestCase


class TestScoreController(BaseTestCase):
    """ScoreController integration test stubs"""

    def test_delete_score(self):
        """Test case for delete_score

        Delete a previously uploaded node score
        """
        response = self.client.open(
            '/deregnet/score/{score_id}'.format(score_id='score_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_score(self):
        """Test case for get_score

        Retrieve information on a previously uploaded score
        """
        response = self.client.open(
            '/deregnet/score/{score_id}'.format(score_id='score_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_scores(self):
        """Test case for get_scores

        List available previously uploaded node scores
        """
        query_string = [('searchString', 'searchString_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/deregnet/scores',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_score(self):
        """Test case for post_score

        Upload a node score for use with DeRegNet algorithms
        """
        body = Score()
        response = self.client.open(
            '/deregnet/score',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()