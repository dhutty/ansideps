# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import check_output


def test_forward_deps():
    '''Test forward (descendant) dependencies.'''
    result = run_cmd("python ansideps.py elk")
    deps = result.rstrip('\n').split('\n')
    assert sorted(deps) == sorted(['elasticsearch', 'logstash', 'kibana'])


def test_reverse_deps():
    '''Test reverse (ancestor) dependencies.'''
    result = run_cmd("python ansideps.py --reverse elk")
    deps = result.rstrip('\n').split('\n')
    assert sorted(deps) == sorted(['logvault'])


def run_cmd(cmd):
    '''Run a shell command `cmd` and return its output.'''
    return check_output(cmd, shell=True).decode('utf-8')
