# -*- coding: utf-8 -*-

from opensearchmock import behaviour
from tests import TestOpensearchmock


class TestOpensearchmockBehaviour(TestOpensearchmock):

    def tearDown(self):
        behaviour.disable_all()
