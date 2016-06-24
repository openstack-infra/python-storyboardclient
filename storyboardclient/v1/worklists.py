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

from storyboardclient import base


class FilterCriterion(base.BaseObject):
    field = None
    filter_id = None
    negative = None
    title = None
    value = None


class FilterCriterionNestedManager(base.BaseNestedManager):
    resource_class = FilterCriterion

    # if the method with the filter parameter is called,
    # create the criteria objects using the data received
    # when querying for the worklist
    def get_all_from_filter(self, filter):
        critlist = filter.filter_criteria
        return [FilterCriterion(self, info=crit) for crit in critlist]


class WorklistFilter(base.BaseObject):
    # the query object
    list_filter_criteria = FilterCriterionNestedManager
    # the raw data that is sent
    filter_criteria = None
    list_id = None
    type = None


class WorklistFilterNestedManager(base.BaseNestedManager):
    url_key = "filters"
    parent_url_key = "worklists"
    resource_class = WorklistFilter


class Worklist(base.BaseObject):
    title = None
    creator_id = None
    project_id = None
    private = None
    archived = None
    automatic = None
    filters = None
    users = None
    owners = None
    items = None
    list_filters = WorklistFilterNestedManager


class WorklistItem:
    archived = None
    list_position = None
    list_id = None
    item_id = None
    item_type = None
    display_due_date = None
    resolved_due_date = None


class WorklistsManager(base.BaseManager):
    url_key = "worklists"
    resource_class = Worklist
