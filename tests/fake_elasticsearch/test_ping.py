# -*- coding: utf-8 -*-

from tests import TestOpensearchmock


class TestPing(TestOpensearchmock):

    def test_should_return_true_when_ping(self):
        self.assertTrue(self.os.ping())
