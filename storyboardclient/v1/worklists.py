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
from storyboardclient.v1.tasks import Task
from storyboardclient.v1.stories import Story

class FilterCriterion(base.BaseObject):
    field = None
    filter_id = None
    negative = None
    title = None
    value = None
    type = None


class FilterCriterionNestedManager(base.BaseNestedManager):
    resource_class = FilterCriterion

    # if the method with the filter parameter is called,
    # create the criteria objects using the data received
    # when querying for the worklist
    def get_all_from_filter(self, filter):
        return [FilterCriterion(self, info=crit) for crit in filter.filter_criteria]


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


class WorklistItem(base.BaseObject):
    archived = None
    list_position = None
    list_id = None
    item_id = None
    item_type = None
    display_due_date = None
    resolved_due_date = None
    
    # the field 'item_type' should send either 'story' or
    # 'task' depending on the context. there should also be
    # a field by the name of either one of these which has
    # the actual object as it's value.
    
    # instead of keeping it as a dict, we create the object 
    # and store it in the same place. note that, however, 
    # since 'story' and 'task' are not defined above, the 
    # value of 'item_type' must be checked to find out whether 
    #item.story or item.task is the object that this item 
    # refers to.
    def _add_details(self, info):
        obj_type = info["item_type"]
        if obj_type == "task":
            task = Task(self.manager.client.tasks, info[obj_type], loaded=True)
            setattr(self, obj_type, task)
            del info[obj_type]
        elif obj_type == "story":
            story = Story(self.manager.client.stories, info[obj_type], loaded=True)
            setattr(self, obj_type, story)
            del info[obj_type]
        else: # unsupported type
            raise TypeError(field)

        super(WorklistItem, self)._add_details(info)

# there is also an endpoint at worklists/id/items, however, at
# the moment, we just create the items from the payload that was  
class WorklistItemNestedManager(base.BaseNestedManager):
    resource_class = WorklistItem

    # create the criteria objects using the data received
    # when querying for the worklist
    def get_all_from_worklist(self, worklist):
        return [WorklistItem(self, info=item) for item in worklist.items]


class Worklist(base.BaseObject):
    title = None
    creator_id = None
    project_id = None
    private = None
    archived = None
    automatic = None
    users = None
    owners = None
    # the raw data that is sent
    items = None
    # the query object
    list_items = WorklistItemNestedManager
    list_filters = WorklistFilterNestedManager


class WorklistsManager(base.BaseManager):
    url_key = "worklists"
    resource_class = Worklist
