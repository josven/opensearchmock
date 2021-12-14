# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

import opensearchpy

from opensearchmock import opensearchmock

INDEX_NAME = 'test_index'
DOC_TYPE = 'doc-Type'
DOC_ID = 'doc-id'
BODY = {
    'author': 'kimchy',
    'text': 'Opensearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}


class TestOpensearchmock(unittest.TestCase):

    @opensearchmock
    def setUp(self):
        self.os = opensearchpy.OpenSearch(hosts=[{'host': 'localhost', 'port': 9200}])
