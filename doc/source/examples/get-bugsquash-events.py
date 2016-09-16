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


# This script allows you to see how many actions a user took in
# a set period. You could filter further on the actions to derive
# 'number of stories edited', etc.
# This is a very slow script, because get_all() for timeline events
# currently fails. Therefore, we check the events for each story.
# You might want to stick some print statements early in to check
# it's working.
# This assumes you know the ids of the people whose
# work you wish to track.

from storyboardclient.v1 import client

storyboard = client.Client(api_url="https://storyboard.openstack.org/api/v1")

clarkb_events = []
pleia2_events = []
bkero_events = []

# These are just IDs I obtained manually. You could work them out.

clarkb_id = 38
pleia2_id = 162
bkero_id = 1120

# There is probably no way to work these out. :)
bugsquash_dates= ['2016-09-14', '2016-09-15']

# We get all stories in the instance first so we can scan their
# events. This is faster than querying the api for each story!
stories = storyboard.stories.get_all()

# We use a try: except: block because an exception will be raised
# when a story is not found. As stories can be removed, this
# is a common occurence and we shouldn't worry about it.
try:

    # The python client currently can only get timeline events by
    # story, so we go through each story and get all of its
    # events
    for story in stories:
        events = story.events.get_all()

        # Once we have the list of events for a story, we check for all
        # events that occurred in a certain timeframe
        for event in events:

            # This gets all events that happened across the two bugsquash days.
            # The date is only part of the event.created_at field, which
            # includes a time (eg: '2016-02-26T13:35:42+00:00').
            # You could go further and narrow by timestamps if necessary, or
            # use event ids if you knew which corresponded with the times.
            for date in bugsquash_dates:
                if date in event.created_at:


                    # We push events created by each person during the bugsquash
                    # into their own array so we can count them (and filter further
                    # if we want to). We print the numbers as we go along to
                    # create an exciting race. You could order them by quantity if
                    # you really wanted, or animate a race in pygame.
                    if event.author_id == clarkb_id:
                        clarkb_events.append(event)
                        print "clarkb: %d" % len(clarkb_events)
                        print "pleia2: %d" % len(pleia2_events)
                        print "bkero: %d" % len(bkero_events)



                    if event.author_id == pleia2_id:
                        pleia2_events.append(event)
                        print "pleia2: %d" % len(pleia2_events)
                        print "clarkb: %d" % len(clarkb_events)
                        print "bkero: %d" % len(bkero_events)


                    if event.author_id == bkero_id:
                        bkero_events.append(event)
                        print "bkero: %d" % len(bkero_events)
                        print "clarkb: %d" % len(clarkb_events)
                        print "pleia2: %d" % len(pleia2_events)



except:
    pass

# Print the grand totals at the end
print "pleia2: %d" % len(pleia2_events)
print "clarkb: %d" % len(clarkb_events)
print "bkero: %d" % len(bkero_events)
