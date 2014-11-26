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

from storyboardclient import base
from storyboardclient.tests import base as test_base


class BaseObjectTestCase(test_base.TestCase):

    def test_init_no_nested(self):
        manager_mock = mock.MagicMock()
        obj = base.BaseObject(manager=manager_mock, info={"id": "test_id"})

        self.assertEqual("test_id", obj.id)
        self.assertEqual(manager_mock, obj.manager)

    def test_init_with_nested(self):

        manager_mock = mock.MagicMock()

        class TestInheritedObject(base.BaseObject):
            manager_field = base.BaseNestedManager

        obj = TestInheritedObject(manager=manager_mock, info={"id": "test_id"})

        self.assertEqual(base.BaseNestedManager, type(obj.manager_field))

        self.assertEqual("test_id", obj.id)
        self.assertEqual("test_id", obj.manager_field.parent_id)
