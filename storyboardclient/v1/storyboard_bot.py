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
import gerritlib.gerrit
import re

storyboard = client.Client(api_url="http://0.0.0.0:9000/api/v1", access_token="PUT AN ACCESS TOKEN HERE")

# much of the following stolen and adjusted from:
# https://github.com/mtreinish/germqtt/blob/master/germqtt/germqtt.py
# I took things and generally made them worse. (I only wanted to take
# the bits I needed and understood, but this is probably less robust
class GerritStream(object):

    def __init__(self, user, host, key, port=29418):
        self.gerrit = gerritlib.gerrit.Gerrit(host, user, port, key)
        self.gerrit.startWatching()

    def get_event(self):
        return self.gerrit.getEvent()
def main():
    gerrit = GerritStream("Zara", "review.openstack.org", "/home/ubuntu/.ssh/gerritymcgerritson", port=29418)
    while True:
        event = gerrit.get_event()
        if event:
            updateRelevantThings(event.items())

def updateRelevantThings(eventItems):
    for key, value in eventItems:
        if (key=="change"):
           status = value.get('status')
           message = value.get('commitMessage')
           owner = value.get('owner')
           if (status == "NEW"):
               newStatus = "review"
           elif (status == "SUBMITTED"):
               newStatus = "review"
           elif (status == "ABANDONED"):
               newStatus = "todo"
           elif (status == "MERGED"):
               newStatus = "merged"
           identity = getTaskID(message)
           storyboard.tasks.update(id=identity, status=newStatus, link=message)

def getTaskID(message):
# This regexp business is shamelessly stolen and adjusted from:
# https://git.openstack.org/cgit/openstack-infra/jeepyb/tree/jeepyb/cmd/update_bug.py#n301
# It's mostly witchcraft to me and I recommend asking jeblair about it.
# Anyway, this version should just match the word 'task: ' if it's at the start of a line,
# and return the numbers following that. If for some odd reason you list multiple tasks,
# it'll only alter the first one listed
    part1 = r'^[\t ]*(?P<prefix>[-\w]+)?[\s:]*'
    part2 = r'(?:\b(?:task)\b[\s#:]*)+'
    part3 = r'(?P<bug_number>\d+)\s*?$'
    regexp = part1 + part2 + part3
    matches = re.finditer(regexp, message, flags=re.I | re.M)
    for match in matches:
        bug_num = match.group('bug_number')
        print "updating task " bug_num
        return bug_num
    return 42 #this is just here so it doesn't error when the regexp isn't matched,
#              because I missed the course on error handling and wound up studying
#              Descartes instead. it updates task 42 with the latest change. Will
#              fail if task is not found in storyboard. There's a fix for this in
#              jeepyb code, I just didn't understand it enough to steal it yet.
    
main()
