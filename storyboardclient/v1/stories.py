# Copyright (c) 2015 Mirantis Inc.
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
from storyboardclient.v1 import tags as tags_api
from storyboardclient.v1 import tasks
from storyboardclient.v1 import timeline


class Story(base.BaseObject):
    title = None
    description = None
    is_bug = None
    creator_id = None
    status = None
    tags = None
    story_type_id = None
    private = None

    tasks = tasks.TasksNestedManager
    comments = timeline.CommentsNestedManager
    events = timeline.TimeLineEventsNestedManager
    tags_manager = tags_api.TagsNestedManager


class StoriesManager(base.BaseManager):
    url_key = "stories"
    resource_class = Story
