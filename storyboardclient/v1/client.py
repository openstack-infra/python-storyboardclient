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
from storyboardclient.v1 import branches
from storyboardclient.v1 import milestones
from storyboardclient.v1 import project_groups
from storyboardclient.v1 import projects
from storyboardclient.v1 import stories
from storyboardclient.v1 import subscription_events
from storyboardclient.v1 import subscriptions
from storyboardclient.v1 import tags
from storyboardclient.v1 import tasks
from storyboardclient.v1 import teams
from storyboardclient.v1 import users
from storyboardclient.v1 import worklists


class Client(base.BaseClient):
    """A client class for StoryBoard.

    Usage example:
    @code:
        from storyboard.v1 import client

        storyboard = client.Client("https://storyboard.openstack.org/api/v1",
                                   "mytoken")
    """

    def __init__(self, api_url=None, access_token=None):
        """Sets up a client with endpoint managers.

        :param api_url: (Optional) Full API url. Defaults to
        https://storyboard.openstack.org/api/v1
        :param access_token: (Optional) OAuth2 access token. If skipped only
        public read-only endpoint will be available. All other requests will
        fail with Unauthorized error.
        :return: a client instance.
        """
        super(Client, self).__init__(api_url=api_url,
                                     access_token=access_token)

        self.branches = branches.BranchesManager(self)
        self.tasks = tasks.TasksManager(self)
        self.teams = teams.TeamsManager(self)
        self.projects = projects.ProjectsManager(self)
        self.project_groups = project_groups.ProjectGroupsManager(self)
        self.stories = stories.StoriesManager(self)
        self.users = users.UsersManager(self)
        self.subscription_events = \
            subscription_events.SubscriptionEventsManager(self)
        self.subscriptions = subscriptions.SubscriptionsManager(self)
        self.tags = tags.TagsManager(self)
        self.milestones = milestones.MilestonesManager(self)
        self.worklists = worklists.WorklistsManager(self)
