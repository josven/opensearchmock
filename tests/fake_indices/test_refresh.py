# -*- coding: utf-8 -*-

from tests import TestOpensearchmock, INDEX_NAME


class TestRefresh(TestOpensearchmock):

    def test_should_refresh_index(self):
        self.os.indices.create(INDEX_NAME)
        self.os.indices.refresh(INDEX_NAME)
        self.assertTrue(self.os.indices.exists(INDEX_NAME))
