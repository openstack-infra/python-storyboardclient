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
from storyboardclient.v1 import stories


class StoriesTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.stories.StoriesManager._list")
    def test_stories_list(self, mock_private_list):
        mock_private_list.return_value = [
            stories.Story(mock.MagicMock(),
                          info={"name": "test_story"}),
            stories.Story(mock.MagicMock(),
                          info={"name": "test_story_2"})]
        stories_list = stories.StoriesManager(mock.MagicMock()).list()

        self.assertEqual(2, len(stories_list))

    @mock.patch("storyboardclient.v1.stories.StoriesManager._post")
    def test_stories_create(self, mock_private_post):
        stories.StoriesManager(mock.MagicMock()).create(
            name="test_pg")

        mock_private_post.assert_called_once_with("/stories",
                                                  {"name": "test_pg"})

    @mock.patch("storyboardclient.v1.stories.StoriesManager._put")
    def test_stories_update(self, mock_private_put):
        stories.StoriesManager(mock.MagicMock()).update(
            id="story_id",
            name="test_story_updated")

        mock_private_put.assert_called_once_with(
            "/stories/story_id",
            {"name": "test_story_updated"})

    @mock.patch("storyboardclient.v1.tasks.TasksNestedManager._list")
    def test_stories_list_tasks(self, mock_private_list):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})

        test_story.tasks.list()

        # A strange None here stands for the collection_key which is supposed
        # to be there but is not required for StoryBoard
        mock_private_list.assert_called_once_with(
            "/stories/test_story_id/tasks", None)

    @mock.patch("storyboardclient.v1.tasks.TasksNestedManager._post")
    def test_stories_create_task(self, mock_private_post):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})

        test_story.tasks.create(title="test_task")

        mock_private_post.assert_called_once_with(
            "/stories/test_story_id/tasks",
            {"title": "test_task",
             "story_id": "test_story_id"})

    @mock.patch(
        "storyboardclient.v1.timeline.TimeLineEventsNestedManager._list"
    )
    def test_stories_list_events(self, mock_private_list):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})

        test_story.events.list()

        mock_private_list.assert_called_once_with(
            "/stories/test_story_id/events", None)

    @mock.patch("storyboardclient.v1.timeline.CommentsNestedManager._list")
    def test_stories_list_comments(self, mock_private_list):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})

        test_story.comments.list()

        mock_private_list.assert_called_once_with(
            "/stories/test_story_id/comments", None)

    @mock.patch("storyboardclient.v1.timeline.CommentsNestedManager._post")
    def test_stories_create_comment(self, mock_private_post):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})

        test_story.comments.create(content="test_comment")

        mock_private_post.assert_called_once_with(
            "/stories/test_story_id/comments",
            {"content": "test_comment"})

    @mock.patch("storyboardclient.v1.timeline.CommentsNestedManager._put")
    def test_stories_update_comment(self, mock_private_put):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})
        test_story.comments.update(id="comment_id",
                                   content="updated_test_comment")

        mock_private_put.assert_called_once_with(
            "/stories/test_story_id/comments/comment_id",
            {"content": "updated_test_comment"})

    @mock.patch("storyboardclient.v1.tags.TagsNestedManager._put")
    def test_stories_update_tags(self, mock_private_put):
        test_story = stories.Story(mock.MagicMock(),
                                   info={"id": "test_story_id"})
        test_story.tags_manager.update(["first_test_tag", "second_test_tag"])

        mock_private_put.assert_called_once_with(
            "/stories/test_story_id/tags",
            ["first_test_tag", "second_test_tag"])
