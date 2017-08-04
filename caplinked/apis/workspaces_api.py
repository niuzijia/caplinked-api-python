# coding: utf-8

"""
    CapLinked API v1.0

    Core information security endpoints for managing files/folders, users/groups, uploads/downloads, and more.

    OpenAPI spec version: 2017-05-23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class WorkspacesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_workspaces(self, team_id, **kwargs):
        """
        List all workspaces for a team
        List all workspaces for a team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workspaces(team_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int team_id: ID of team from which to list workspaces (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_workspaces_with_http_info(team_id, **kwargs)
        else:
            (data) = self.get_workspaces_with_http_info(team_id, **kwargs)
            return data

    def get_workspaces_with_http_info(self, team_id, **kwargs):
        """
        List all workspaces for a team
        List all workspaces for a team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workspaces_with_http_info(team_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int team_id: ID of team from which to list workspaces (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in params) or (params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `get_workspaces`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team_id' in params:
            query_params.append(('team_id', params['team_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/workspaces', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Workspace',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_workspaces_id(self, id, **kwargs):
        """
        Get workspace information
        Get workspace information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workspaces_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of workspace (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_workspaces_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_workspaces_id_with_http_info(id, **kwargs)
            return data

    def get_workspaces_id_with_http_info(self, id, **kwargs):
        """
        Get workspace information
        Get workspace information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workspaces_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of workspace (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspaces_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_workspaces_id`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/workspaces/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Workspace',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_workspaces(self, team_id, workspace_name, **kwargs):
        """
        Create workspace
        Create workspace. Workspace creator will be added to Workspace Admins group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workspaces(team_id, workspace_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int team_id: ID of parent team for this workspace (required)
        :param str workspace_name: Name of workspace to create (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_workspaces_with_http_info(team_id, workspace_name, **kwargs)
        else:
            (data) = self.post_workspaces_with_http_info(team_id, workspace_name, **kwargs)
            return data

    def post_workspaces_with_http_info(self, team_id, workspace_name, **kwargs):
        """
        Create workspace
        Create workspace. Workspace creator will be added to Workspace Admins group.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workspaces_with_http_info(team_id, workspace_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int team_id: ID of parent team for this workspace (required)
        :param str workspace_name: Name of workspace to create (required)
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id', 'workspace_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workspaces" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in params) or (params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `post_workspaces`")
        # verify the required parameter 'workspace_name' is set
        if ('workspace_name' not in params) or (params['workspace_name'] is None):
            raise ValueError("Missing the required parameter `workspace_name` when calling `post_workspaces`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'team_id' in params:
            form_params.append(('team_id', params['team_id']))
        if 'workspace_name' in params:
            form_params.append(('workspace[name]', params['workspace_name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/workspaces', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Workspace',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_workspaces_id(self, id, **kwargs):
        """
        Update workspace
        Update workspace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_workspaces_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of workspace to update (required)
        :param str workspace_name: Name of workspace to update
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_workspaces_id_with_http_info(id, **kwargs)
        else:
            (data) = self.put_workspaces_id_with_http_info(id, **kwargs)
            return data

    def put_workspaces_id_with_http_info(self, id, **kwargs):
        """
        Update workspace
        Update workspace
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_workspaces_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of workspace to update (required)
        :param str workspace_name: Name of workspace to update
        :return: Workspace
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'workspace_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_workspaces_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `put_workspaces_id`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'workspace_name' in params:
            form_params.append(('workspace[name]', params['workspace_name']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/workspaces/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Workspace',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)