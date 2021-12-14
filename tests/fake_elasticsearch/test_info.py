# -*- coding: utf-8 -*-

from tests import TestOpensearchmock


class TestInfo(TestOpensearchmock):

    def test_should_return_status_200_for_info(self):
        info = self.os.info()
        self.assertEqual(info.get('status'), 200)
