# -*- coding: utf-8 -*-

import opensearchpy

from opensearchmock import opensearchmock
from opensearchmock.fake_opensearch import FakeOpensearch
from tests import TestOpensearchmock


class TestInstance(TestOpensearchmock):

    def test_should_create_fake_opensearch_instance(self):
        self.assertIsInstance(self.os, FakeOpensearch)

    @opensearchmock
    def test_should_return_same_opensearch_instance_when_instantiate_more_than_one_instance_with_same_host(self):
        es1 = opensearchpy.OpenSearch(hosts=[{'host': 'localhost', 'port': 9200}])
        es2 = opensearchpy.OpenSearch(hosts=[{'host': 'localhost', 'port': 9200}])
        self.assertEqual(es1, es2)
