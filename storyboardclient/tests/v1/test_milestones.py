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
from storyboardclient.v1 import milestones


class MilestonesTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.milestones.MilestonesManager._list")
    def test_milestones_list(self, mock_private_list):
        milestones.MilestonesManager(mock.MagicMock()).list()

        mock_private_list.assert_called_once_with(
            "/milestones", None)

    @mock.patch("storyboardclient.v1.milestones.MilestonesManager._post")
    def test_milestones_create(self, mock_private_post):
        milestones.MilestonesManager(mock.MagicMock()).create(
            name="test_milestone",
            branch_id="test_branch_id")

        mock_private_post.assert_called_once_with(
            "/milestones",
            {"name": "test_milestone",
             "branch_id": "test_branch_id"})

    @mock.patch("storyboardclient.v1.milestones.MilestonesManager._put")
    def test_milestones_update(self, mock_private_put):
        milestones.MilestonesManager(mock.MagicMock()).update(
            id="test_milestone_id",
            name="test_milestone_updated")

        mock_private_put.assert_called_once_with(
            "/milestones/test_milestone_id",
            {"name": "test_milestone_updated"})
