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

storyboard = client.Client(api_url="http://0.0.0.0:9000/api/v1", access_token="ZARA'S SUPER SECRET ACCESS TOKEN")

gerritThing = gerrit.Gerrit("review.openstack.org", "Zara", port=29418, keyfile="/home/ubuntu/.ssh/gerritymcgerritson")

gerritWatcher = gerritThing.startWatching()
gerritEvents = gerritThing.getEvent()

def msgAndStatus(events):
    for key, value in gerritEvents.items():
       if (key=="change"):
          status = value.get('status')
          commitMessage = value.get('commitMessage')
          return status, commitMessage

gerritStatusMessage = msgAndStatus(gerritEvents)
status, message = gerritStatusMessage

def storyboardUpdater(stat, msg):
    if (stat == "NEW"):
        newStatus = "review"
    elif (stat == "SUBMITTED"):
        newStatus = "review"
    elif (stat == "ABANDONED"):
        newStatus = "todo"
    elif (stat == "MERGED"):
        newStatus = "merged"
    storyboard.tasks.update(id=42, title="hi how are you", status=newStatus, link=msg)


storyboardUpdater(status, message)
