=====
Usage
=====

To use python-storyboardclient in a project::

    from storyboardclient.v1 import client
    storyboard = client.Client(api_url="http://storyboard-dev.openstack.org/api/v1", access_token="MY_ACCESS_TOKEN")

That will not work with storyboard-dev because of certificates, but that demos the syntax.

To get things::

    get_due_dates_for_board = storyboard.due_dates.get_all(board_id=2)
    get_system_info = storyboard.system_info.get(None)
    get_worklists_in_board = storyboard.worklists.board_id.get(2)
    get_due_dates = storyboard.due_dates.get_all()
    get_stories = storyboard.stories.get_all()
    get_users_in_team = storyboard.teams.get(1).users.get_all()
    get_subscriptions = storyboard.subscriptions.get_all()
    get_comments_on_one_story = storyboard.stories.get(1).comments.list()
    get_tags_on_one_story = storyboard.stories.get(1).tags()
    get_preferences_for_one_user = storyboard.users.get(1).user_preferences.get_all()
    get_subscription_events = storyboard.subscription_events.get_all()
    get_all_story_timeline_events = storyboard.stories.get(1).events.get_all()
    get_worklists = storyboard.worklists.get_all()
    get_tokens_for_one_user = storyboard.users.get(1).user_tokens.list()
    get_milestones = storyboard.milestones.get_all()
    get_branches = storyboard.branches.get_all()



To create things::


    create_story = storyboard.stories.create(title="brand new invalid story with no tasks")
    create_task = storyboard.tasks.create(title="new task with default settings", project_id=2, story_id=3)
    create_branch = storyboard.branches.create(project_id=21, name='newbranch')
    create_worklist = storyboard.worklists.create(title='new worklist', automatic=False)
    create_board = storyboard.boards.create(title="new board", lanes='')




To update things::

   update_branch_title = storyboard.branches.update(id=21, name='new name')
   update_worklist = storyboard.worklists.update(id=296, automatic=True)
   update_board = storyboard.boards.update(id=3, title="new title")

 

Note: there is currently no endpoint for permissions.


Misc example scripts::


    for story in get_stories:
        if "blah" in story.description:
        print story

    for i in range (981277, 2000690):
        try:
            story = storyboard.stories.get(i)
            print story
        except Exception as e:
            print e


TODO:

Sections on updating board and worklist items need filling in.
Timeline events for boards and worklists need adding.

