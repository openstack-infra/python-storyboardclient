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

from storyboardclient._apiclient import auth


class OAuthPlugin(auth.BaseAuthPlugin):

    def _do_authenticate(self, http_client):
        # Skipping for now as there will be a separate spec and implementation
        # for authenticating a python client with OAuth.
        pass

    def __init__(self, api_url=None, access_token=None):
        super(OAuthPlugin, self).__init__()

        self.api_url = api_url
        self.access_token = access_token

    def token_and_endpoint(self, endpoint_type=None, service_type=None):
        return self.access_token, self.api_url
