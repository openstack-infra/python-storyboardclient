# Copyright (c) 2014 Mirantis Inc.
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

from storyboardclient import base
from storyboardclient.tests import base as test_base


class BaseNestedManagerTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.base.BaseManager._get")
    def test_get(self, mock_private_get):
        manager = base.BaseNestedManager(mock.MagicMock(),
                                         parent_id="parent_id")
        manager.parent_url_key = "parent_key"
        manager.url_key = "key"
        manager.get("id1")

        mock_private_get.assert_called_once_with(
            "/parent_key/parent_id/key/id1", None)

    @mock.patch("storyboardclient.base.BaseManager._post")
    def test_create(self, mock_private_post):
        manager = base.BaseNestedManager(mock.MagicMock(),
                                         parent_id="parent_id")
        manager.parent_url_key = "parent_key"
        manager.url_key = "key"
        manager.create(title="test_task")

        mock_private_post.assert_called_once_with(
            "/parent_key/parent_id/key",
            {"title": "test_task"})
