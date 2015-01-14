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
from storyboardclient.v1 import project_groups
from storyboardclient.v1 import projects


class ProjectGroupsTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.project_groups.ProjectGroupsManager."
                "_list")
    def test_project_groups_list(self, mock_private_list):
        mock_private_list.return_value = [
            project_groups.ProjectGroup(mock.MagicMock(),
                                        info={"name": "test_pg"}),
            project_groups.ProjectGroup(mock.MagicMock(),
                                        info={"name": "test_pg_2"})]

        project_groups_list = project_groups.ProjectGroupsManager(
            mock.MagicMock()).list()

        self.assertEqual(2, len(project_groups_list))

    @mock.patch("storyboardclient.v1.project_groups.ProjectGroupsManager."
                "_post")
    def test_project_groups_create(self, mock_private_post):
        project_groups.ProjectGroupsManager(mock.MagicMock()).create(
            name="test_pg")

        mock_private_post.assert_called_once_with("/project_groups",
                                                  {"name": "test_pg"})

    @mock.patch("storyboardclient.v1.project_groups.ProjectGroupsManager."
                "_put")
    def test_project_groups_update(self, mock_private_put):
        project_groups.ProjectGroupsManager(mock.MagicMock()).update(
            id="pg_id",
            name="test_pg_updated")

        mock_private_put.assert_called_once_with(
            "/project_groups/pg_id",
            {"name": "test_pg_updated"})

    @mock.patch("storyboardclient.v1.project_groups.ProjectsNestedManager."
                "_put")
    def test_project_groups_add_project(self, mock_private_put):
        test_project_group = project_groups.ProjectGroup(
            mock.MagicMock(),
            info={"id": "test_pg_id"})

        test_project = projects.Project(mock.MagicMock(),
                                        info={"id": "test_project_id"})
        test_project_group.projects.add(test_project)

        mock_private_put.assert_called_once_with(
            "/project_groups/test_pg_id/projects/test_project_id")

    @mock.patch("storyboardclient.v1.project_groups.ProjectsNestedManager."
                "_delete")
    def test_project_groups_remove_project(self, mock_private_delete):
        test_project_group = project_groups.ProjectGroup(
            mock.MagicMock(),
            info={"id": "test_pg_id"})

        test_project = projects.Project(mock.MagicMock(),
                                        info={"id": "test_project_id"})
        test_project_group.projects.remove(test_project)

        mock_private_delete.assert_called_once_with(
            "/project_groups/test_pg_id/projects/test_project_id")