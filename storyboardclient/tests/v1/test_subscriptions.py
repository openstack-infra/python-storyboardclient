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
from storyboardclient.v1 import subscriptions


class SubscriptionsTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.subscriptions.SubscriptionsManager._list")
    def test_subscriptions_list(self, mock_private_list):
        subscriptions.SubscriptionsManager(mock.MagicMock()).list()

        mock_private_list.assert_called_once_with(
            "/subscriptions", None)

    @mock.patch("storyboardclient.v1.subscriptions.SubscriptionsManager._post")
    def test_subscriptions_create(self, mock_private_post):
        subscriptions.SubscriptionsManager(mock.MagicMock()).create(
            target_type="story",
            target_id="test_story_id")

        mock_private_post.assert_called_once_with(
            "/subscriptions",
            {"target_type": "story",
             "target_id": "test_story_id"})
