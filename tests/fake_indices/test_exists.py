# -*- coding: utf-8 -*-

from tests import TestOpensearchmock, INDEX_NAME


class TestExists(TestOpensearchmock):

    def test_should_return_false_when_index_does_not_exists(self):
        self.assertFalse(self.os.indices.exists(INDEX_NAME))

    def test_should_return_true_when_index_exists(self):
        self.os.indices.create(INDEX_NAME)
        self.assertTrue(self.os.indices.exists(INDEX_NAME))
