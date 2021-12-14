# -*- coding: utf-8 -*-

from tests import TestOpensearchmock, INDEX_NAME


class TestCreate(TestOpensearchmock):

    def test_should_create_index(self):
        self.assertFalse(self.os.indices.exists(INDEX_NAME))
        self.os.indices.create(INDEX_NAME)
        self.assertTrue(self.os.indices.exists(INDEX_NAME))
