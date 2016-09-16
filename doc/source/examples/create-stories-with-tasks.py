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


# This script creates a bunch of stories with tasks. This is useful
# if you want to create a lot of sample stories quickly for testing
# purposes. If you use this in production, you will have bad luck
# for 7 years.

from storyboardclient.v1 import client

# If you use http instead of https, you will get strange errors
api_url="https://storyboard-dev.openstack.org/api/v1"

# This is accessible from the profile page submenu, when logged in
# via the webclient
access_token="$MY_ACCESS_TOKEN"

# For any instance with a self-signed certificate, you will need to
# pass this in order to do POSTs, PUTs, or DELETEs.
verify = False

storyboard = client.Client(api_url, access_token, verify)

# Stories can be removed, so we can't just get the length of the
# stories array. IDs are always sequential, so this gets the id of
# the last item in the stories array.
highest_story_id = storyboard.stories.get_all()[-1].id

# The id for our new story will be the next ID sequentially.
# This is our best guess at what that will be. There is a chance
# this will not be accurate, if the last story in the instance
# has been deleted.
new_story_id = highest_story_id+1


# This should create a number of new stories. Here we're making 100, arbitrarily.
for i in range(100):

    # First, we POST a story. You could add a description, etc, if you wanted.
    # We're setting these titles so we can easily find our new stories.
    new_story = storyboard.stories.create(title = "autocreated story with id %d" % new_story_id)

    # We could stop here and POST tasks later, but the stories will be
    # invalid until they have tasks, and will not be associated with any
    # projects-- so they'll be harder to find later.
    # So, next, we POST a task, and associate it with that story via
    # the story_id. Here we're arbitrarily selecting a project, project 2, to
    # associate the task with. Again, you could set things, like task
    # statuses, if you wanted. If you don't, they'll be the default ('todo').
    storyboard.tasks.create(title = "autocreated task for story %d" % new_story.id, project_id = 2, story_id = new_story.id)

    # Finally, increment new story ID, and repeat.
    new_story_id += 1
