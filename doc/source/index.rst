=========================
 python-storyboardclient
=========================

This is the StoryBoard python client! It lets you interact with
StoryBoard from the comfort of your own terminal! There is no
command to run this; instead you can import it into scripts. This
lets you perform complex actions on things in StoryBoard, eg: add an
helpful comment on all stories with 'cannot store contact information'
in the description, pointing users at the relevant docs, but only
if there is no comment to this effect already. (There is an example
of such a script in :doc:`usage`)

Some sample commands are given in :doc:`usage`. In general, most
resources (ie: stories, tasks, projects, and so on)
have a ``get_all()`` and ``get()`` method. The latter takes
the resource's id as a parameter, thought it can also take
other attributes (eg: tag name).

To create a new resource, use the ``create()`` method. The
necessary parameters depend on the resource, and if not
documented, can be worked out from the relevant .py
file in the code for the StoryBoard API.

The ``update()`` method will update mutable fields of the resource (again,
these vary depending on the resource).

Finally, ``delete()`` will delete things.

Happy task-tracking!

Contents:

.. toctree::
   :maxdepth: 2

   installation
   usage
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
