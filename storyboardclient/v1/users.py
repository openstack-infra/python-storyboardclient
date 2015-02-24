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

from storyboardclient import base
from storyboardclient.v1 import user_preferences
from storyboardclient.v1 import user_tokens


class User(base.BaseObject):
    username = None
    full_name = None
    openid = None
    is_superuser = None
    last_login = None
    enable_login = None

    user_preferences = user_preferences.UserPreferencesManager
    user_tokens = user_tokens.UserTokensNestedManager


class UsersManager(base.BaseManager):
    url_key = "users"
    resource_class = User
