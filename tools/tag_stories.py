#!/usr/bin/env python3

import os.path
import warnings

import appdirs

import storyboardconfig

warnings.filterwarnings(
    'ignore',
    '.*Unverified HTTPS request is being made.*',
)

def _update_tags(sbc, story, tag):
    tags = set(story.tags or [])
    if tag in tags:
        return
    if not tag:
        return
    tags.add(tag)
    if None in tags:
        tags.remove(None)
    # print('setting tags to {}'.format(tags))
    try:
        print('adding', tag)
        story.tags_manager.update(list(sorted((tags))))
        #story.tags_manager.update([tag])
    except Exception as err:
        print('Failed to update tags:', err)


config_dir = appdirs.user_config_dir('storyboard', 'OpenStack')
config_file = os.path.join(config_dir, 'storyboard.ini')

config = storyboardconfig.get_config(config_file)

sbc = storyboardconfig.get_client(config)

team_name = 'oslo'

story = sbc.stories.get('1531530')

print(story)
for task in story.tasks.get_all():
    print()
    print(story.id, task.id, task.title, task.priority)

    tag_name = 'priority-{}-{}'.format(team_name, task.priority)

    _update_tags(sbc, story, tag_name)

print()

# project_groups = sbc.project_groups.get_all(name='oslo')
# project_group = project_groups[0]

# stories = {}

# def _get_story(sbc, id):
#     if id not in stories:
#         story = sbc.stories.get(id)
#         stories[id] = story
#     return stories[id]

# for project in project_group.projects.get_all():
#     for task in sbc.tasks.get_all(project_id=project.id):
#         story = _get_story(sbc, task.story_id)
#         print(project.name, story.id, task.id, task.title)
#         tag_name = 'priority-{}-{}'.format(team_name, task.priority)
#         _update_tags(sbc, story, tag_name)
