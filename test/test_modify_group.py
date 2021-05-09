# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group())
    app.group.modify_first_group(Group(name="Newgroup"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group())
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group())
    app.group.modify_first_group(Group(name="Secondgroup", header="Secondgroup", footer="Secondgroup"))


