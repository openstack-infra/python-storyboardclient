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

from storyboardclient import base
from storyboardclient.openstack.common._i18n import _LW  # noqa
from storyboardclient.openstack.common import log

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

    def get_one(self, key):
        """Get User Preference by key.

        :return: The preference value or None if not set
        """

        all_prefs = super(UserPreferencesManager, self).get(None)
        return getattr(all_prefs, key)

    def get(self, id):
        LOG.warn(_LW("You are probably using a wrong method to get "
                     "UserPreferences. User preferences are always fetched in "
                     "a bundle. See get_all method. To get a preference by key"
                     " use get_one method."))
        return super(UserPreferencesManager, self).get(id)

    def set(self, data):
        """Set a dictionary of user preferences.

        """

        return self.create(**data)

    def set_one(self, key, value):
        """Set a user preference by key.

        """

        return self.set({key: value})

    def remove_one(self, key):
        """Removes a property from user preferences.

        """

        return self.set({key: None})
