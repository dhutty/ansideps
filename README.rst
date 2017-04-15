========
ansideps
========

.. image:: https://badge.fury.io/py/ansideps.png
    :target: http://badge.fury.io/py/ansideps

.. image:: https://travis-ci.org/dhutty/ansideps.png?branch=master
        :target: https://travis-ci.org/dhutty/ansideps

.. image:: https://pypip.in/d/ansideps/badge.png
        :target: https://crate.io/packages/ansideps?version=latest


Resolve Ansible role relationships.

* use `--help` for usage instructions.

Features
--------

* takes one or more role names, creates a graph of the relationships between the roles in the Ansible roles_path and returns the dependencies (ancestor or descendant)
* can also write dot (graphviz) files with the entire graph.

Requirements
------------

- Python >= 2.6 or >= 3.3

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/dhutty/ansideps/blob/master/LICENSE>`_ file.
