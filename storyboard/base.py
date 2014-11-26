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

import six

from storyboard.openstack.common._i18n import _
from storyboard.openstack.common.apiclient import base
from storyboard.openstack.common.apiclient import client
from storyboard.auth import oauth

DEFAULT_API_URL = "http://storyboard.openstack.org/api/v1"


class BaseClient(client.BaseClient):

    def __init__(self, api_url=None, access_token=None):
        if not api_url:
            api_url = DEFAULT_API_URL

        self.auth_plugin = oauth.OAuthPlugin(api_url, access_token)
        self.http_client = BaseHTTPClient(auth_plugin=self.auth_plugin, verify=False)


class BaseHTTPClient(client.HTTPClient):
    """
    This HTTP client is overriding a client_request method to add
    Authorization header if OAuth token is provided.

    """
    def client_request(self, client, method, url, **kwargs):
        """Send an http request using `client`'s endpoint and specified `url`.

        If request was rejected as unauthorized (possibly because the token is
        expired), issue one authorization attempt and send the request once
        again.

        :param client: instance of BaseClient descendant
        :param method: method of HTTP request
        :param url: URL of HTTP request
        :param kwargs: any other parameter that can be passed to
            `HTTPClient.request`
        """

        token, endpoint = (self.cached_token, client.cached_endpoint)
        if not (token and endpoint):
            token, endpoint = self.auth_plugin.token_and_endpoint()
            self.cached_token = token
            client.cached_endpoint = endpoint

        if token:
            kwargs.setdefault("headers", {})["Authorization"] = \
                "Bearer %s" % token

        return self.request(method, self.concat_url(endpoint, url), **kwargs)


class BaseManager(base.CrudManager):

    id = None
    created_at = None
    updated_at = None

    def build_url(self, base_url=None, **kwargs):
        # Overriding to use "url_key" instead of the "collection_key".
        # "key_id" is replaced with just "id" when querying a specific object.
        url = base_url if base_url is not None else ''

        url += '/%s' % getattr(self, "url_key")

        entity_id = kwargs.get('id')
        if entity_id is not None:
            url += '/%s' % entity_id

        return url

    def get(self, id):
        """
        Get method is accepting id as a positional argument for simplicity.

        :param id: The id of resource.
        :return: The resource object.
        """

        query_kwargs = {"id": id}
        return self._get(self.build_url(**query_kwargs), self.key)



class BaseObject(base.Resource):

    def _add_details(self, info):
        for field, value in six.iteritems(info):

            # Skip the fields which are not declared in the object
            if not hasattr(self, field):
                continue

            setattr(self, field, value)
