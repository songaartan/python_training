# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Newgroup"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group(app):
    app.group.modify_first_group(Group(name="Secondgroup", header="Secondgroup", footer="Secondgroup"))
