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

import mock

from storyboardclient.tests import base as test_base
from storyboardclient.v1 import tasks


class TasksTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.tasks.TasksManager._list")
    def test_tasks_list(self, mock_private_list):
        mock_private_list.return_value = [
            tasks.Task(mock.MagicMock(),
                       info={"title": "test_task"}),
            tasks.Task(mock.MagicMock(),
                       info={"title": "test_task_2"})]

        teams_list = tasks.TasksManager(mock.MagicMock()).list()

        self.assertEqual(2, len(teams_list))

    @mock.patch("storyboardclient.v1.tasks.TasksManager._post")
    def test_tasks_create(self, mock_private_post):
        tasks.TasksManager(mock.MagicMock()).create(
            title="test_task",
            story_id="test_story_id",
            project_id="test_project_id",
            branch_id="test_branch_id")

        mock_private_post.assert_called_once_with(
            "/tasks",
            {"title": "test_task",
             "story_id": "test_story_id",
             "project_id": "test_project_id",
             "branch_id": "test_branch_id"})

    @mock.patch("storyboardclient.v1.tasks.TasksManager._put")
    def test_tasks_update(self, mock_private_put):
        tasks.TasksManager(mock.MagicMock()).update(
            id="task_id",
            title="test_task_updated")

        mock_private_put.assert_called_once_with(
            "/tasks/task_id",
            {"title": "test_task_updated"})

    @mock.patch("storyboardclient.v1.tasks.TasksManager._delete")
    def test_tasks_delete(self, mock_private_delete):
        tasks.TasksManager(mock.MagicMock()).delete(id="task_id")

        mock_private_delete.assert_called_once_with("/tasks/task_id")
