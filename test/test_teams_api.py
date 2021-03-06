# coding: utf-8

"""
    CapLinked API v1.0

    Core information security endpoints for managing files/folders, users/groups, uploads/downloads, and more.

    OpenAPI spec version: 2017-05-23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import caplinked
from caplinked.rest import ApiException
from caplinked.apis.teams_api import TeamsApi


class TestTeamsApi(unittest.TestCase):
    """ TeamsApi unit test stubs """

    def setUp(self):
        self.api = caplinked.apis.teams_api.TeamsApi()

    def tearDown(self):
        pass

    def test_delete_teams_id_memberships(self):
        """
        Test case for delete_teams_id_memberships

        Remove team member
        """
        pass

    def test_get_teams(self):
        """
        Test case for get_teams

        List all teams in organization
        """
        pass

    def test_get_teams_id(self):
        """
        Test case for get_teams_id

        Get team information
        """
        pass

    def test_get_teams_id_memberships(self):
        """
        Test case for get_teams_id_memberships

        Get list of team members
        """
        pass

    def test_get_teams_id_watermark_settings(self):
        """
        Test case for get_teams_id_watermark_settings

        List custom watermarks for a team
        """
        pass

    def test_post_teams(self):
        """
        Test case for post_teams

        Create team
        """
        pass

    def test_post_teams_id_memberships(self):
        """
        Test case for post_teams_id_memberships

        Add team member
        """
        pass

    def test_put_teams_id(self):
        """
        Test case for put_teams_id

        Update team
        """
        pass


if __name__ == '__main__':
    unittest.main()
