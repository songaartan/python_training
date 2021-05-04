# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="Firstgroup", header="Firstgroup", footer="Firstgroup"))
    app.session.logout()