# -*- coding: utf-8 -*-

from opensearchmock.behaviour import server_failure


def disable_all():
    server_failure.disable()
