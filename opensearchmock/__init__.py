# -*- coding: utf-8 -*-

from functools import wraps

from opensearchpy.client import _normalize_hosts
from unittest.mock import patch

from opensearchmock.fake_opensearch import FakeOpensearch

ELASTIC_INSTANCES = {}


def _get_elasticmock(hosts=None, *args, **kwargs):
    host = _normalize_hosts(hosts)[0]
    elastic_key = '{0}:{1}'.format(
        host.get('host', 'localhost'), host.get('port', 9200)
    )

    if elastic_key in ELASTIC_INSTANCES:
        connection = ELASTIC_INSTANCES.get(elastic_key)
    else:
        connection = FakeOpensearch()
        ELASTIC_INSTANCES[elastic_key] = connection
    return connection


def opensearchmock(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        ELASTIC_INSTANCES.clear()
        with patch('opensearchpy.OpenSearch', _get_elasticmock):
            result = f(*args, **kwargs)
        return result
    return decorated
