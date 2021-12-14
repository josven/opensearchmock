# -*- coding: utf-8 -*-

from opensearchmock import behaviour
from tests.fake_elasticsearch.behaviour import TestOpensearchmockBehaviour
from tests import INDEX_NAME, DOC_TYPE, BODY


class TestBehaviourServerFailure(TestOpensearchmockBehaviour):

    def test_should_return_internal_server_error_when_simulate_server_error_is_true(self):
        behaviour.server_failure.enable()
        data = self.os.index(index=INDEX_NAME, doc_type=DOC_TYPE, body=BODY)

        expected = {
            'status_code': 500,
            'error': 'Internal Server Error'
        }

        self.assertDictEqual(expected, data)
