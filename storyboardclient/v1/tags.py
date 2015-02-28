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

from storyboardclient import base


class Tag(base.BaseObject):
    name = None


class TagsManager(base.BaseManager):
    url_key = "tags"
    resource_class = Tag


class TagsNestedManager(base.BaseNestedManager):
    parent_url_key = "stories"
    url_key = "tags"
    resource_class = Tag

    def update(self, tags):
        return self._put(self.build_url(), tags)

    def delete(self, tags):
        return self.client.delete(self.build_url(), json=tags)
