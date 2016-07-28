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



# absolutely horrible WIP commandline interface for the python client.
# use it by typing 'storyboard.$thingyouwant.$method', at the prompt, eg:
# storyboard.stories.get_all() . It can optionally take an access token
# as a commandline argument if you give it one when starting up

#storyboard-dev doesn't actually work with this, because of certificates
#strangeness. I've kept that as the example since I really don't want
#people accidentally spamming storyboard.o.o with a million POSTs.

from storyboardclient.v1 import client
import sys

api_url= ''
access_token = ''

def main(args):
    api_url = args[0]
    try:
        access_token = args[1]
    except:
        access_token = None

    storyboard = client.Client(api_url, access_token)
    while True==True:
        command = input('What would you like this lovely python client to do today?')
        if command == help:
            usage = 'Commands are of the form "storyboard.$resource.$method", eg: "storyboard.stories.get(1)"'
            print usage
        try:
            print command
        except:
            pass

if len(sys.argv) == 1:
    print "Error! you need to say where storyboard lives, eg: python commandline.py http://storyboard-dev.openstack.org/api/v1"
else:
    main(sys.argv[1:])
#storyboard = client.Client(api_url="http://0.0.0.0:9000/api/v1", access_token="McflZWz76w5REriKAhBjrsdOqwhwgF")
