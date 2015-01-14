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
from storyboardclient.v1 import projects


class ProjectsNestedManager(base.BaseNestedManager):
    parent_url_key = "project_groups"
    url_key = "projects"
    resource_class = projects.Project

    def add(self, project):
        """Add a Project to the Project Group.

        :param project: can be a Project instance or id
        :return: the result of Project Group update operation
        """

        if isinstance(project, projects.Project):
            project_id = project.id
        else:
            project_id = project

        self.put(id=project_id)

    def remove(self, project):
        """Remove a Project from a Project Group.

        :param project: can be a Project instance or id
        :return: the result of Project Group update operation
        """

        if isinstance(project, projects.Project):
            project_id = project.id
        else:
            project_id = project

        self.delete(id=project_id)


class ProjectGroup(base.BaseObject):
    name = None
    title = None

    projects = ProjectsNestedManager


class ProjectGroupsManager(base.BaseManager):
    url_key = "project_groups"
    resource_class = ProjectGroup
