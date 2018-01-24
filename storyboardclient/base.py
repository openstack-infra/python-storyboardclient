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

import inspect

import six

from storyboardclient._apiclient import base
from storyboardclient._apiclient import client
from storyboardclient.auth import oauth

DEFAULT_API_URL = "https://storyboard-dev.openstack.org/api/v1"


class BaseClient(client.BaseClient):

    def __init__(self, api_url=None, access_token=None, verify=True):
        if not api_url:
            api_url = DEFAULT_API_URL

        self.auth_plugin = oauth.OAuthPlugin(api_url, access_token)
        self.http_client = BaseHTTPClient(auth_plugin=self.auth_plugin,
                                          verify=verify)


class BaseHTTPClient(client.HTTPClient):
    """Base class for setting up endpoint and token.

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

    def build_url(self, base_url=None, method=None, **kwargs):
        # Overriding to use "url_key" instead of the "collection_key".
        # "key_id" is replaced with just "id" when querying a specific object.
        url = base_url if base_url is not None else ''

        url += '/%s' % self.url_key

        entity_id = kwargs.get('id')
        if entity_id is not None:
            url += '/%s' % entity_id

        elif method == 'get':
            first = True
            for key, value in six.iteritems(kwargs):
                if first:
                    url += '?'
                    first = False
                else:
                    url += '&'
                url += '%s=%s' % (key, value)

        return url

    def get(self, id):
        """Get a resource by id.

        Get method is accepting id as a positional argument for simplicity.

        :param id: The id of resource.
        :return: The resource object.
        """

        query_kwargs = {"id": id}
        return self._get(self.build_url(**query_kwargs), self.key)

    def get_all(self, **kwargs):
        """Get resources by properties other than ID."""
        kwargs = self._filter_kwargs(kwargs)
        return self._get_all(self.build_url(method='get', **kwargs), self.key)

    def _get_all(self, url, response_key=None):
        """Get collection of stuff.

        Put here because we can't modify base.py in the OpenStack
        APIclient (probably)

        :param url: a partial URL, e.g., '/servers'
        :param response_key: the key to be looked up in response dictionary,
            e.g., 'server'. If response_key is None - all response body
            will be used.
        """

        body = self.client.get(url).json()
        data = body[response_key] if response_key is not None else body
        return [self.resource_class(self, item, loaded=True) for item in data]

    def create(self, **kwargs):
        """Create a resource.

        The default implementation is overridden so that the dictionary is
        passed 'as is' without any wrapping.
        """

        kwargs = self._filter_kwargs(kwargs)
        return self._post(self.build_url(**kwargs), kwargs)

    def update(self, **kwargs):
        """Update a resource.

        The default implementation is overridden so that the dictionary is
        passed 'as is' without any wrapping. The id field is removed from the
        request body.
        """

        kwargs = self._filter_kwargs(kwargs)
        params = kwargs.copy()
        params.pop('id')

        return self._put(self.build_url(**kwargs), params)


class BaseNestedManager(BaseManager):

    def __init__(self, client, parent_id):
        super(BaseNestedManager, self).__init__(client)

        self.parent_id = parent_id

    def build_url(self, base_url=None, **kwargs):
        # Overriding to use "url_key" instead of the "collection_key".
        # "key_id" is replaced with just "id" when querying a specific object.
        url = base_url if base_url is not None else ''

        url += '/%s/%s/%s' % (self.parent_url_key, self.parent_id,
                              self.url_key)

        entity_id = kwargs.get('id')
        if entity_id is not None:
            url += '/%s' % entity_id

        return url


class BaseObject(base.Resource):

    id = None
    created_at = None
    updated_at = None

    def __init__(self, manager, info, loaded=False, parent_id=None):
        super(BaseObject, self).__init__(manager, info, loaded)

        self._parent_id = parent_id
        self._init_nested_managers()

    def _add_details(self, info):
        for field, value in six.iteritems(info):

            # Skip the fields which are not declared in the object
            if not hasattr(self, field):
                continue

            setattr(self, field, value)

    def _init_nested_managers(self):
        # If an object has nested resource managers, they will be initialized
        # here.

        manager_instances = {}

        for manager_name, manager_class in self._managers():
            manager_instance = manager_class(client=self.manager.client,
                                             parent_id=self.id)
            # Saving a manager to a dict as self.__dict__ should not be
            # changed while iterating
            manager_instances[manager_name] = manager_instance

        for name, manager_instance in six.iteritems(manager_instances):
            # replacing managers declarations with real managers
            setattr(self, name, manager_instance)

    def _managers(self):
        # Iterator over nested managers

        for attr in dir(self):
            # Skip private fields
            if attr.startswith("_"):
                continue
            val = getattr(self, attr)
            if inspect.isclass(val) and issubclass(val, BaseNestedManager):
                yield attr, val
