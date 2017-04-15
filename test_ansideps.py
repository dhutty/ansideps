# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import check_output


def test_forward_deps():
    '''Test forward (descendant) dependencies.'''
    result = run_cmd("ansideps elk")
    assert result == "elasticsearch\nlogstash\nkibana\n"


def test_reverse_deps():
    '''Test reverse (ancestor) dependencies.'''
    result = run_cmd("ansideps --reverse elk")
    assert result == "logvault\n"


def run_cmd(cmd):
    '''Run a shell command `cmd` and return its output.'''
    return check_output(cmd, shell=True).decode('utf-8')
