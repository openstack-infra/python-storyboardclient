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


class Task(base.BaseObject):
    title = None
    status = None
    is_active = None
    creator_id = None
    story_id = None
    project_id = None
    assignee_id = None
    branch_id = None
    milestone_id = None
    priority = None
    link = None


class TasksManager(base.BaseManager):
    url_key = "tasks"
    resource_class = Task


class TasksNestedManager(base.BaseNestedManager):
    parent_url_key = "stories"
    url_key = "tasks"
    resource_class = Task

    def create(self, **kwargs):
        kwargs["story_id"] = self.parent_id
        return super(TasksNestedManager, self).create(**kwargs)
