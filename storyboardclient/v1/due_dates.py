# Copyright (c) 2016 Codethink Ltd.
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


class DueDate(base.BaseObject):
    name = None
    date = None
    private = None
    creator_id = None
    permissions = None  # Not yet included in python client
    tasks = None
    stories = None
    boards = None  # Not yet mapped in python client
    worklists = None  # Not yet mapped in python client


class DueDatesManager(base.BaseManager):
    url_key = "due_dates"
    resource_class = DueDate
