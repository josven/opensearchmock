# -*- coding: utf-8 -*-

from tests import TestOpensearchmock, INDEX_NAME


class TestDelete(TestOpensearchmock):

    def test_should_delete_index(self):
        self.assertFalse(self.os.indices.exists(INDEX_NAME))

        self.os.indices.create(INDEX_NAME)
        self.assertTrue(self.os.indices.exists(INDEX_NAME))

        self.os.indices.delete(INDEX_NAME)
        self.assertFalse(self.os.indices.exists(INDEX_NAME))

    def test_should_delete_inexistent_index(self):
        self.assertFalse(self.os.indices.exists(INDEX_NAME))

        self.os.indices.delete(INDEX_NAME)
        self.assertFalse(self.os.indices.exists(INDEX_NAME))
