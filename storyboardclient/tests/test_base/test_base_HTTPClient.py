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

from storyboardclient.auth import oauth
from storyboardclient import base
from storyboardclient.tests import base as test_base


class BaseHTTPClientTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.base.BaseHTTPClient.request")
    def test_unauthorized_client_request(self, mock_request):

        auth_plugin = oauth.OAuthPlugin(api_url="http://some_endpoint")
        client = base.BaseHTTPClient(auth_plugin=auth_plugin)

        client.client_request(client=mock.MagicMock(),
                              method="GET", url="/some_url")

        mock_request.assert_called_once_with("GET",
                                             "http://some_endpoint/some_url")

    @mock.patch("storyboardclient.base.BaseHTTPClient.request")
    def test_authorized_client_request(self, mock_request):

        auth_plugin = oauth.OAuthPlugin(api_url="http://some_endpoint",
                                        access_token="some_token")
        client = base.BaseHTTPClient(auth_plugin=auth_plugin)

        client.client_request(client=mock.MagicMock(),
                              method="GET", url="/some_url")

        mock_request.assert_called_once_with(
            "GET",
            "http://some_endpoint/some_url",
            headers={
                "Authorization": "Bearer some_token"
            })
