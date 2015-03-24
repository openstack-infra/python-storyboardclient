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
from storyboardclient.v1 import subscription_events


class SubscriptionEventsTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1."
                "subscription_events.SubscriptionEventsManager._list")
    def test_subscription_events_list(self, mock_private_list):
        subscription_events.SubscriptionEventsManager(mock.MagicMock()).list()

        mock_private_list.assert_called_once_with(
            "/subscription_events", None)

    @mock.patch("storyboardclient.v1."
                "subscription_events.SubscriptionEventsManager._get")
    def test_subscription_events_get(self, mock_private_get):
        subscription_events.SubscriptionEventsManager(mock.MagicMock()).\
            get("test_subscription_event_id")

        mock_private_get.assert_called_once_with(
            "/subscription_events/test_subscription_event_id", None)

    @mock.patch("storyboardclient.v1."
                "subscription_events.SubscriptionEventsManager._delete")
    def test_subscription_events_delete(self, mock_private_delete):
        subscription_events.SubscriptionEventsManager(mock.MagicMock()).\
            delete(id="test_subscription_event_id")

        mock_private_delete.assert_called_once_with(
            "/subscription_events/test_subscription_event_id")
