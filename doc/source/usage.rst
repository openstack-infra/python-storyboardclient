=====
Usage
=====

To use python-storyboardclient in a project::

    from storyboardclient.v1 import client
    api_url="https://storyboard-dev.openstack.org/api/v1"
    access_token="$MY_ACCESS_TOKEN"
    storyboard = client.Client(api_url, access_token)


The access token is optional, but needed for creating things,
updating things, or retrieving private information.  It is very
important to use https, not http, or you will get weird and wonderful
errors!

The 'verify' setting is necessary for accessing instances using
self-signed certificates (including storyboard-dev). So, for such
instances, you would need to adjust the above example to include::

    verify = False
    storyboard = client.Client(api_url, access_token, verify)


Some sample commands to get things::

    get_stories = storyboard.stories.get_all()
    get_comments_on_one_story = storyboard.stories.get(1).comments.list()
    get_tags_on_one_story = storyboard.stories.get(1).tags()
    get_all_story_timeline_events = storyboard.stories.get(1).events.get_all()
    get_worklists = storyboard.worklists.get_all()
    get_worklists_in_board = storyboard.worklists.board_id.get(2)
    get_due_dates = storyboard.due_dates.get_all()
    get_due_dates_for_board = storyboard.due_dates.get_all(board_id=2)
    get_users_in_team = storyboard.teams.get(1).users.get_all()
    get_subscriptions = storyboard.subscriptions.get_all()
    get_preferences_for_one_user = storyboard.users.get(1).user_preferences.get_all()
    get_subscription_events = storyboard.subscription_events.get_all()
    get_tokens_for_one_user = storyboard.users.get(1).user_tokens.list()
    get_milestones = storyboard.milestones.get_all()
    get_branches = storyboard.branches.get_all()
    get_system_info = storyboard.system_info.get(None)




Some sample commands to create things::


    create_story = storyboard.stories.create(title="brand new invalid story with no tasks")
    create_task = storyboard.tasks.create(title="new task with default settings", project_id=2, story_id=3)
    create_branch = storyboard.branches.create(project_id=21, name='newbranch')
    create_worklist = storyboard.worklists.create(title='new worklist', automatic=False)
    create_board = storyboard.boards.create(title="new board", lanes='')




Some sample commands to update things::

   update_branch_title = storyboard.branches.update(id=21, name='new name')
   update_worklist = storyboard.worklists.update(id=296, automatic=True)
   update_board = storyboard.boards.update(id=3, title="new title")



Note: there is currently no single endpoint for permissions of the form
      api/v1/permissions. There are endpoints specific to some resources, eg:
      api/v1/worklists/1/permissions . The python client does not support
      these yet (patches welcome!).


Misc example script-snippets::


    get_stories = storyboard.stories.get_all()
    for story in get_stories:
        if "blah" in story.description:
        print story

    for i in range (981277, 2000690):
        try:
            story = storyboard.stories.get(i)
            print story
        except Exception as e:
            print e

Longer sample script::

    from storyboardclient.v1 import client

    storyboard = client.Client(api_url="https://storyboard-dev.openstack.org/api/v1", access_token="$MY_ACCESS_TOKEN")

    stories = storyboard.stories.get_all()

    for story in stories:
        try:
            if 'Cannot store contact information' in story.description and 'Friendlybot' not in story.description:
                story.comments.create(content="This needs your gerrit preferred e-mail address to match a primary e-mail address for a foundation individual member account.\n \n If you already followed the instructions at http://docs.openstack.org/infra/manual/developers.html#account-setup - in the specified order! - and still get that, see https://ask.openstack.org/question/56720 for additional troubleshooting tips.")
                storyboard.stories.update(id=story.id, description=story.description + '\n \n Friendlybot was here!')
        except:
            pass

TODO:

Sections on updating board and worklist items need filling in.
Timeline events for boards and worklists need adding.
