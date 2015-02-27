# Copyright (c) 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock

from storyboardclient.tests import base as test_base
from storyboardclient.v1 import branches


class BranchesTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.branches.BranchesManager._list")
    def test_branches_list(self, mock_private_list):
        branches.BranchesManager(mock.MagicMock()).list()

        mock_private_list.assert_called_once_with(
            "/branches", None)

    @mock.patch("storyboardclient.v1.branches.BranchesManager._post")
    def test_branches_create(self, mock_private_post):
        branches.BranchesManager(mock.MagicMock()).create(
            name="test_branch",
            project_id="test_project_id")

        mock_private_post.assert_called_once_with(
            "/branches",
            {"name": "test_branch",
             "project_id": "test_project_id"})

    @mock.patch("storyboardclient.v1.branches.BranchesManager._put")
    def test_branches_update(self, mock_private_put):
        branches.BranchesManager(mock.MagicMock()).update(
            id="test_branch_id",
            name="test_branch_updated")

        mock_private_put.assert_called_once_with(
            "/branches/test_branch_id",
            {"name": "test_branch_updated"})
