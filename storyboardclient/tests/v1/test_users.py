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
from storyboardclient.v1 import users


class UserTestCase(test_base.TestCase):

    @mock.patch(
        "storyboardclient.v1.user_tokens.UserTokensNestedManager._list"
    )
    def test_user_list_tokens(self, mock_private_list):
        user = users.User(manager=mock.MagicMock(), info={"id": "test_id"})

        user.user_tokens.list()

        mock_private_list.assert_called_once_with(
            "/users/test_id/tokens", None)

    @mock.patch(
        "storyboardclient.v1.user_tokens.UserTokensNestedManager._post"
    )
    def test_user_create_token(self, mock_private_post):
        user = users.User(manager=mock.MagicMock(), info={"id": "test_id"})

        user.user_tokens.create(expires_in=300, user_id="test_id")

        mock_private_post.assert_called_once_with(
            "/users/test_id/tokens",
            {"expires_in": 300,
             "user_id": "test_id"})

    @mock.patch("storyboardclient.v1.user_tokens.UserTokensNestedManager._put")
    def test_user_update_token(self, mock_private_put):
        user = users.User(manager=mock.MagicMock(), info={"id": "test_id"})

        user.user_tokens.update(id="test_token_id", expires_in=500)

        mock_private_put.assert_called_once_with(
            "/users/test_id/tokens/test_token_id",
            {"expires_in": 500})
