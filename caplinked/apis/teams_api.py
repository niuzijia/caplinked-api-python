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


class TeamsApi(object):
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

    def delete_teams_id_memberships(self, id, user_id, **kwargs):
        """
        Remove team member
        Remove team member
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_teams_id_memberships(id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team from which user will be removed (required)
        :param int user_id: ID of user to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_teams_id_memberships_with_http_info(id, user_id, **kwargs)
        else:
            (data) = self.delete_teams_id_memberships_with_http_info(id, user_id, **kwargs)
            return data

    def delete_teams_id_memberships_with_http_info(self, id, user_id, **kwargs):
        """
        Remove team member
        Remove team member
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_teams_id_memberships_with_http_info(id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team from which user will be removed (required)
        :param int user_id: ID of user to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_teams_id_memberships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_teams_id_memberships`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_teams_id_memberships`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/teams/{id}/memberships', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_teams(self, **kwargs):
        """
        List all teams in organization
        List all teams in organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_teams_with_http_info(**kwargs)
        else:
            (data) = self.get_teams_with_http_info(**kwargs)
            return data

    def get_teams_with_http_info(self, **kwargs):
        """
        List all teams in organization
        List all teams in organization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_teams" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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

        return self.api_client.call_api('/teams', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Team',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_teams_id(self, id, **kwargs):
        """
        Get team information
        Get team information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the Team (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_teams_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_teams_id_with_http_info(id, **kwargs)
            return data

    def get_teams_id_with_http_info(self, id, **kwargs):
        """
        Get team information
        Get team information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the Team (required)
        :return: Team
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
                    " to method get_teams_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_teams_id`")


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

        return self.api_client.call_api('/teams/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Team',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_teams_id_memberships(self, id, **kwargs):
        """
        Get list of team members
        Get list of team members
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id_memberships(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team for which users will be listed (required)
        :return: list[Membership]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_teams_id_memberships_with_http_info(id, **kwargs)
        else:
            (data) = self.get_teams_id_memberships_with_http_info(id, **kwargs)
            return data

    def get_teams_id_memberships_with_http_info(self, id, **kwargs):
        """
        Get list of team members
        Get list of team members
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id_memberships_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team for which users will be listed (required)
        :return: list[Membership]
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
                    " to method get_teams_id_memberships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_teams_id_memberships`")


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

        return self.api_client.call_api('/teams/{id}/memberships', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Membership]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_teams_id_watermark_settings(self, id, **kwargs):
        """
        List custom watermarks for a team
        List custom watermarks for a team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id_watermark_settings(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team (required)
        :return: CustomWatermarkSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_teams_id_watermark_settings_with_http_info(id, **kwargs)
        else:
            (data) = self.get_teams_id_watermark_settings_with_http_info(id, **kwargs)
            return data

    def get_teams_id_watermark_settings_with_http_info(self, id, **kwargs):
        """
        List custom watermarks for a team
        List custom watermarks for a team
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_teams_id_watermark_settings_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team (required)
        :return: CustomWatermarkSetting
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
                    " to method get_teams_id_watermark_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_teams_id_watermark_settings`")


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

        return self.api_client.call_api('/teams/{id}/watermark_settings', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CustomWatermarkSetting',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_teams(self, team_name, **kwargs):
        """
        Create team
        Create team. Current user will become team owner.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_teams(team_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str team_name: Name of the team (required)
        :param int team_allowed_workspaces: Maximum workspaces for team
        :param int team_allowed_admins: Maximum number of admins for team
        :param bool team_drm_enabled: Toggle DRM (feature availability in workspaces)
        :param bool team_watermarking: Toggle watermarking (feature availability in workspaces)
        :param bool team_suppress_emails: Toggle email invites
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_teams_with_http_info(team_name, **kwargs)
        else:
            (data) = self.post_teams_with_http_info(team_name, **kwargs)
            return data

    def post_teams_with_http_info(self, team_name, **kwargs):
        """
        Create team
        Create team. Current user will become team owner.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_teams_with_http_info(team_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str team_name: Name of the team (required)
        :param int team_allowed_workspaces: Maximum workspaces for team
        :param int team_allowed_admins: Maximum number of admins for team
        :param bool team_drm_enabled: Toggle DRM (feature availability in workspaces)
        :param bool team_watermarking: Toggle watermarking (feature availability in workspaces)
        :param bool team_suppress_emails: Toggle email invites
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_name', 'team_allowed_workspaces', 'team_allowed_admins', 'team_drm_enabled', 'team_watermarking', 'team_suppress_emails']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_teams" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_name' is set
        if ('team_name' not in params) or (params['team_name'] is None):
            raise ValueError("Missing the required parameter `team_name` when calling `post_teams`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'team_name' in params:
            form_params.append(('team[name]', params['team_name']))
        if 'team_allowed_workspaces' in params:
            form_params.append(('team[allowed_workspaces]', params['team_allowed_workspaces']))
        if 'team_allowed_admins' in params:
            form_params.append(('team[allowed_admins]', params['team_allowed_admins']))
        if 'team_drm_enabled' in params:
            form_params.append(('team[drm_enabled]', params['team_drm_enabled']))
        if 'team_watermarking' in params:
            form_params.append(('team[watermarking]', params['team_watermarking']))
        if 'team_suppress_emails' in params:
            form_params.append(('team[suppress_emails]', params['team_suppress_emails']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/teams', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Team',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_teams_id_memberships(self, id, user_id, **kwargs):
        """
        Add team member
        Add team member
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_teams_id_memberships(id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team to which user will be added (required)
        :param int user_id: ID of user to add (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_teams_id_memberships_with_http_info(id, user_id, **kwargs)
        else:
            (data) = self.post_teams_id_memberships_with_http_info(id, user_id, **kwargs)
            return data

    def post_teams_id_memberships_with_http_info(self, id, user_id, **kwargs):
        """
        Add team member
        Add team member
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_teams_id_memberships_with_http_info(id, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team to which user will be added (required)
        :param int user_id: ID of user to add (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_teams_id_memberships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `post_teams_id_memberships`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `post_teams_id_memberships`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'user_id' in params:
            form_params.append(('user_id', params['user_id']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/teams/{id}/memberships', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Membership',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_teams_id(self, id, **kwargs):
        """
        Update team
        Update team. Includes option to designate a new Team Owner.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_teams_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team to update (required)
        :param str team_name: Name of the team
        :param int team_team_owner_id: User ID of the team owner
        :param int team_allowed_workspaces: Maximum workspaces for team
        :param int team_allowed_admins: Maximum number of admins for team
        :param bool team_drm_enabled: Toggle DRM (feature availability in workspaces)
        :param bool team_watermarking: Toggle watermarking (feature availability in workspaces)
        :param bool team_suppress_emails: Toggle email invites
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_teams_id_with_http_info(id, **kwargs)
        else:
            (data) = self.put_teams_id_with_http_info(id, **kwargs)
            return data

    def put_teams_id_with_http_info(self, id, **kwargs):
        """
        Update team
        Update team. Includes option to designate a new Team Owner.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_teams_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of team to update (required)
        :param str team_name: Name of the team
        :param int team_team_owner_id: User ID of the team owner
        :param int team_allowed_workspaces: Maximum workspaces for team
        :param int team_allowed_admins: Maximum number of admins for team
        :param bool team_drm_enabled: Toggle DRM (feature availability in workspaces)
        :param bool team_watermarking: Toggle watermarking (feature availability in workspaces)
        :param bool team_suppress_emails: Toggle email invites
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'team_name', 'team_team_owner_id', 'team_allowed_workspaces', 'team_allowed_admins', 'team_drm_enabled', 'team_watermarking', 'team_suppress_emails']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_teams_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `put_teams_id`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'team_name' in params:
            form_params.append(('team[name]', params['team_name']))
        if 'team_team_owner_id' in params:
            form_params.append(('team[team_owner_id]', params['team_team_owner_id']))
        if 'team_allowed_workspaces' in params:
            form_params.append(('team[allowed_workspaces]', params['team_allowed_workspaces']))
        if 'team_allowed_admins' in params:
            form_params.append(('team[allowed_admins]', params['team_allowed_admins']))
        if 'team_drm_enabled' in params:
            form_params.append(('team[drm_enabled]', params['team_drm_enabled']))
        if 'team_watermarking' in params:
            form_params.append(('team[watermarking]', params['team_watermarking']))
        if 'team_suppress_emails' in params:
            form_params.append(('team[suppress_emails]', params['team_suppress_emails']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/teams/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Team',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
