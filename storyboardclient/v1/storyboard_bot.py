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

from storyboardclient.v1 import client

from pprint import pprint
from gerritlib import gerrit

storyboard = client.Client(api_url="http://0.0.0.0:9000/api/v1", access_token="REDACTED")

gerritThing = gerrit.Gerrit("review.openstack.org", "Zara", port=29418, keyfile="/home/ubuntu/.ssh/gerritymcgerritson")

gerritWatcher = gerritThing.startWatching(connection_attempts=-1, retry_delay=5)
gerritEvents = gerritThing.getEvent()

def getDetailsFromGerrit(events):
    for key, value in gerritEvents.items():
       if (key=="change"):
          status = value.get('status')
          message = value.get('commitMessage')
          owner = value.get('owner')       
          return status, message, owner #Owner is a dict, others are strings
 
#StatusMessageOwner = getDetailsFromGerrit(gerritEvents)
status, message, owner = getDetailsFromGerrit(gerritEvents)

#TODO: thing to map 'owner' to storyboard user id
#TODO: thing to check commit message for text matching regexp (eg: task_id=435)
# if commitMessage contains task_id=, get characters between = and end of line
#TODO: sort out this control flow. It miiiight be okay now

def storyboardUpdater(status, message, owner):
    if (status == "NEW"):
        newStatus = "review"
    elif (status == "SUBMITTED"):
        newStatus = "review"
    elif (status == "ABANDONED"):
        newStatus = "todo"
    elif (status == "MERGED"):
        newStatus = "merged"
    storyboard.tasks.update(id=42, status=newStatus, link=message) #TODO: add assignee =owner.thing, match id to commit task id


while True==True:
    storyboardUpdater(status, message, owner) #'owner' doesn't do anything yet, but we'd like to make the task assignee the owner in the end
    gerritEvents = gerritThing.getEvent()
    status, message, owner = getDetailsFromGerrit(gerritEvents)
#lines above kinda work, break after a bit. Whenever it can't find what it's looking for, this script crashes.
