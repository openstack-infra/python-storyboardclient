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

import mock

from storyboardclient.tests import base as test_base
from storyboardclient.v1 import teams
from storyboardclient.v1 import users


class TeamsTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.teams.TeamsManager._list")
    def test_teams_list(self, mock_private_list):
        mock_private_list.return_value = [
            teams.Team(mock.MagicMock(), info={"name": "test_team"}),
            teams.Team(mock.MagicMock(), info={"name": "test_team_2"})]

        teams_list = teams.TeamsManager(mock.MagicMock()).list()

        self.assertEqual(2, len(teams_list))

    @mock.patch("storyboardclient.v1.teams.TeamsManager._post")
    def test_teams_create(self, mock_private_post):
        teams.TeamsManager(mock.MagicMock()).create(name="test_team")

        mock_private_post.assert_called_once_with("/teams",
                                                  {"name": "test_team"})

    @mock.patch("storyboardclient.v1.teams.TeamsManager._put")
    def test_teams_update(self, mock_private_put):
        teams.TeamsManager(mock.MagicMock()).update(id="team_id",
                                                    name="test_team_updated")

        mock_private_put.assert_called_once_with(
            "/teams/team_id",
            {"name": "test_team_updated"})

    @mock.patch("storyboardclient.v1.teams.UsersNestedManager._put")
    def test_teams_add_user(self, mock_private_put):
        test_team = teams.Team(mock.MagicMock(),
                               info={"id": "test_team_id"})

        test_user = users.User(mock.MagicMock(), info={"id": "test_user_id"})
        test_team.users.add(test_user)

        mock_private_put.assert_called_once_with(
            "/teams/test_team_id/users/test_user_id")

    @mock.patch("storyboardclient.v1.teams.UsersNestedManager._delete")
    def test_teams_delete_user(self, mock_private_delete):
        test_team = teams.Team(mock.MagicMock(),
                               info={"id": "test_team_id"})

        test_user = users.User(mock.MagicMock(), info={"id": "test_user_id"})
        test_team.users.remove(test_user)

        mock_private_delete.assert_called_once_with(
            "/teams/test_team_id/users/test_user_id")