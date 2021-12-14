# -*- coding: utf-8 -*-

from tests import TestOpensearchmock, DOC_TYPE


class TestCount(TestOpensearchmock):

    def test_should_return_count_for_indexed_documents_on_index(self):
        index_quantity = 0
        for i in range(0, index_quantity):
            self.os.index(index='index_{0}'.format(i), doc_type=DOC_TYPE, body={'data': 'test_{0}'.format(i)})

        count = self.os.count()
        self.assertEqual(index_quantity, count.get('count'))

    def test_should_count_in_multiple_indexes(self):
        self.os.index(index='groups', doc_type='groups', body={'budget': 1000})
        self.os.index(index='users', doc_type='users', body={'name': 'toto'})
        self.os.index(index='pcs', doc_type='pcs', body={'model': 'macbook'})

        result = self.os.count(index=['users', 'pcs'])
        self.assertEqual(2, result.get('count'))

    def test_should_count_with_empty_doc_types(self):
        self.os.index(index='index', doc_type=DOC_TYPE, body={'data': 'test'})
        count = self.os.count(doc_type=[])
        self.assertEqual(1, count.get('count'))

    def test_should_return_skipped_shards(self):
        self.os.index(index='index', doc_type=DOC_TYPE, body={'data': 'test'})
        count = self.os.count(doc_type=[])
        self.assertEqual(0, count.get('_shards').get('skipped'))

    def test_should_count_with_doc_types(self):
        self.os.index(index='index', doc_type=DOC_TYPE, body={'data': 'test1'})
        self.os.index(index='index', doc_type='different-doc-type', body={'data': 'test2'})
        count = self.os.count(doc_type=DOC_TYPE)
        self.assertEqual(1, count.get('count'))
