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

from storyboardclient.tests import base as test_base
from storyboardclient.v1 import user_preferences
from storyboardclient.v1 import users


class UserPreferencesTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.user_preferences.UserPreferencesManager"
                "._get")
    def test_user_preferences_get(self, mock_private_get):
        mock_private_get.return_value = user_preferences.UserPreferences(
            mock.MagicMock(),
            info={"k1": "v1"})

        user = users.User(manager=mock.MagicMock(), info={"id": "test_id"})

        preferences = user.user_preferences.get_all()
        self.assertEqual("v1", preferences.k1)

        p_k1 = user.user_preferences.get("k1")
        self.assertEqual("v1", p_k1)

    @mock.patch("storyboardclient.v1.user_preferences.UserPreferencesManager"
                "._post")
    def test_user_preferences_set(self, mock_private_post):
        user = users.User(manager=mock.MagicMock(), info={"id": "test_id"})

        user.user_preferences.set({"k1": "v1"})
        mock_private_post.assert_called_once_with("/users/test_id/preferences",
                                                  {"k1": "v1"})
