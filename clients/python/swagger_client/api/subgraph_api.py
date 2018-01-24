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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient

import os
import requests
import igraph as ig

class SubgraphApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_subgraph(self, subgraph_id, **kwargs):  # noqa: E501
        """Delete a previously found subgraph  # noqa: E501

        Deletes a subgraph  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_subgraph(subgraph_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: ID of the order that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_subgraph_with_http_info(subgraph_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_subgraph_with_http_info(subgraph_id, **kwargs)  # noqa: E501
            return data

    def delete_subgraph_with_http_info(self, subgraph_id, **kwargs):  # noqa: E501
        """Delete a previously found subgraph  # noqa: E501

        Deletes a subgraph  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_subgraph_with_http_info(subgraph_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: ID of the order that needs to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subgraph_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subgraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subgraph_id' is set
        if ('subgraph_id' not in params or
                params['subgraph_id'] is None):
            raise ValueError("Missing the required parameter `subgraph_id` when calling `delete_subgraph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subgraph_id' in params:
            path_params['subgraph_id'] = params['subgraph_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subgraph/{subgraph_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def subgraph_as_igraph(self, subgraph_id, save_graphml_to=None):
        host = self.api_client.configuration.host
        response = requests.get(host+'/subgraph/%s/graphml' % subgraph_id)
        if response.status_code != 200:
            print('Something went wrong!')
            return 'ERROR'
        local_file = os.path.expanduser(os.path.join('~', '.deregnet', 'temporary', '%s.graphml' % subgraph_id)) \
                     if not save_graphml_to else save_graphml_to
        if not local_file.endswith('.graphml'):
            local_file = os.path.join(local_file, '%s.graphml' % subgraph_id)
        with open(local_file, 'wb') as f:
            f.write(response.content)
        subgraph = ig.Graph.Read_GraphML(local_file)
        os.remove(local_file)
        return subgraph



    def download_subgraph_as(self, subgraph_id, filetype, **kwargs):  # noqa: E501
        """Download a subgraph  # noqa: E501

        With this GET Request you will retrieve a subgraph     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.download_subgraph_as(subgraph_id, filetype, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: The Name of the graph (required)
        :param str filetype: File type of file to be downloaded (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.download_subgraph_as_with_http_info(subgraph_id, filetype, **kwargs)  # noqa: E501
        else:
            (data) = self.download_subgraph_as_with_http_info(subgraph_id, filetype, **kwargs)  # noqa: E501
            return data

    def download_subgraph_as_with_http_info(self, subgraph_id, filetype, **kwargs):  # noqa: E501
        """Download a subgraph  # noqa: E501

        With this GET Request you will retrieve a subgraph     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.download_subgraph_as_with_http_info(subgraph_id, filetype, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: The Name of the graph (required)
        :param str filetype: File type of file to be downloaded (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subgraph_id', 'filetype']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_subgraph_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subgraph_id' is set
        if ('subgraph_id' not in params or
                params['subgraph_id'] is None):
            raise ValueError("Missing the required parameter `subgraph_id` when calling `download_subgraph_as`")  # noqa: E501
        # verify the required parameter 'filetype' is set
        if ('filetype' not in params or
                params['filetype'] is None):
            raise ValueError("Missing the required parameter `filetype` when calling `download_subgraph_as`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subgraph_id' in params:
            path_params['subgraph_id'] = params['subgraph_id']  # noqa: E501
        if 'filetype' in params:
            path_params['filetype'] = params['filetype']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subgraph/{subgraph_id}/{filetype}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subgraph(self, subgraph_id, **kwargs):  # noqa: E501
        """Retrieve the information about a subgraph  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subgraph(subgraph_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: ID of subgraph about which to retrieve information (required)
        :return: SubgraphInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subgraph_with_http_info(subgraph_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_subgraph_with_http_info(subgraph_id, **kwargs)  # noqa: E501
            return data

    def get_subgraph_with_http_info(self, subgraph_id, **kwargs):  # noqa: E501
        """Retrieve the information about a subgraph  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subgraph_with_http_info(subgraph_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str subgraph_id: ID of subgraph about which to retrieve information (required)
        :return: SubgraphInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subgraph_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subgraph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subgraph_id' is set
        if ('subgraph_id' not in params or
                params['subgraph_id'] is None):
            raise ValueError("Missing the required parameter `subgraph_id` when calling `get_subgraph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subgraph_id' in params:
            path_params['subgraph_id'] = params['subgraph_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subgraph/{subgraph_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubgraphInfo',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_subgraphs(self, **kwargs):  # noqa: E501
        """List available found subgraphs  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subgraphs(async=True)
        >>> result = thread.get()

        :param async bool
        :param str search_string: pass an optional search string for narrowing the list
        :param int skip: number of records to skip for pagination
        :param int limit: maximum number of records to return
        :return: list[SubgraphInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subgraphs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_subgraphs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_subgraphs_with_http_info(self, **kwargs):  # noqa: E501
        """List available found subgraphs  # noqa: E501

        Returns a single pet  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subgraphs_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str search_string: pass an optional search string for narrowing the list
        :param int skip: number of records to skip for pagination
        :param int limit: maximum number of records to return
        :return: list[SubgraphInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_string', 'skip', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subgraphs" % key
                )
            params[key] = val
        del params['kwargs']

        if 'skip' in params and params['skip'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `skip` when calling `get_subgraphs`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'limit' in params and params['limit'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_subgraphs`, must be a value less than or equal to `50`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_subgraphs`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_string' in params:
            query_params.append(('searchString', params['search_string']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subgraphs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SubgraphInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
