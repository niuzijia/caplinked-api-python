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
from caplinked.apis.downloads_api import DownloadsApi


class TestDownloadsApi(unittest.TestCase):
    """ DownloadsApi unit test stubs """

    def setUp(self):
        self.api = caplinked.apis.downloads_api.DownloadsApi()

    def tearDown(self):
        pass

    def test_delete_downloads_id(self):
        """
        Test case for delete_downloads_id

        Delete download
        """
        pass

    def test_get_downloads_file_file_id(self):
        """
        Test case for get_downloads_file_file_id

        Get single file
        """
        pass

    def test_get_downloads_id(self):
        """
        Test case for get_downloads_id

        Get zip
        """
        pass

    def test_get_downloads_status_workspace_id(self):
        """
        Test case for get_downloads_status_workspace_id

        Get status of downloads for current user
        """
        pass

    def test_post_downloads(self):
        """
        Test case for post_downloads

        Create zip file
        """
        pass


if __name__ == '__main__':
    unittest.main()
