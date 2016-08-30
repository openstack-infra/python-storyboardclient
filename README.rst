=======================
python-storyboardclient
=======================

Python Client library for StoryBoard

* Free software: Apache license
* Documentation: http://docs.openstack.org/infra/storyboard/
* Source: http://git.openstack.org/cgit/openstack-infra/python-storyboardclient
* Bugs: https://storyboard.openstack.org/#!/project/755

Features
--------

* TODO

Notes
--------

This is the StoryBoard python client! It lets you interact with
StoryBoard from the comfort of your own terminal! There is no
command to run this; instead you can import it into scripts. This
lets you perform complex actions on things in StoryBoard, eg: add an
ascii drawing of a cat to all stories with 'bar' in the description
and tag 'baz', created before 2000 CE, but only if there isn't an
ascii frog in the description-- and so on.

Some sample commands are given in usage.rst. In general, most
resources (ie: stories, tasks, projects, and so on)
have a get_all() and get() method. The latter takes
the resource's id as a parameter, thought it can also take
other attributes (eg: tag name).

To create a new resource, use the create() method. The
necessary parameters depend on the resource, and if not
documented, can be worked out from the relevant .py
file in the code for the StoryBoard API.

The update() method will update mutable fields of the resource (again,
these vary depending on the resource).

Happy task-tracking!

