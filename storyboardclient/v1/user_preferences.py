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

from oslo_log import log
import six

from storyboardclient import base

LOG = log.getLogger(__name__)


class UserPreferences(base.BaseObject):

    def _add_details(self, info):
        # User preferences can not be declared before the data is received.
        # Adding all properties to an object directly.
        for key, value in six.iteritems(info):
            setattr(self, key, value)


class UserPreferencesManager(base.BaseNestedManager):
    parent_url_key = "users"
    url_key = "preferences"
    resource_class = UserPreferences

    def get_all(self):
        """Get a dictionary of User Preferences

        User preferences are returned always as a dict, so it's better to use
        a get base method instead of a list here.

        :return: UserPreferences object
        """

        return super(UserPreferencesManager, self).get(None)

    def get(self, key):
        all_prefs = super(UserPreferencesManager, self).get(None)

        return getattr(all_prefs, key)

    def set(self, data):
        """Set a dictionary of user preferences.

        """

        return self.create(**data)

    def set_one(self, key, value):
        """Set a user preference by key.

        """

        return self.set({key: value})
