# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="user1", company="it", address="USA"))


def test_add_empty_contact(app):
    app.contact.create(Contact(name="", company="", address=""))


