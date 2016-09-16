#!/usr/bin/env python
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


# This example script gets all projects in a specified project group
# that have associated tasks. It's possible to filter further by
# task-status. This in turn means the user can see only active
# stories, per project, per project-group.

from storyboardclient.v1 import client

storyboard = client.Client(api_url="http://storyboard.openstack.org/api/v1")

active_projects = []

project_groups = storyboard.project_groups.get_all()

# Get the ID for the desired project group. This example finds active projects
# in the 'openstack-ci' project.
for project_group in project_groups:
    if project_group.name == "openstack-ci":
        group_id = project_group.id

# Get a list of all projects in the desired group.
projects_in_group = storyboard.project_groups.get(group_id).projects.list()

# Filter list by active projects
for task in storyboard.tasks.get_all():

    for project in projects_in_group:

        if task.project_id == project.id and project.name not in active_projects:
            active_projects.append(project.name)

# Print active projects. We don't need a loop, but we use one so that we get 
# nice column that one can easily paste into an etherpad.
for i in active_projects:
    print i
