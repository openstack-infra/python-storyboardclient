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

# This does not get the sha1 or anything useful like that, just the
# numerical version. At time of writing, this is 0.0.1, and may have
# been so for 2 years.

from storyboardclient import base


class SystemInfo(base.BaseObject):
    version = None


class SystemInfoManager(base.BaseManager):
    url_key = "systeminfo"
    resource_class = SystemInfo
