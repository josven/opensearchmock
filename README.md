# OpensearchMock

This is an Opensearch adaption of https://github.com/vrcmarcos/elasticmock


Python Opensearch Mock for test purposes


## Usage

To use OpensearchMock, decorate your test method with **@opensearchmock** decorator:

```python
from unittest import TestCase

from opensearchmock import opensearchmock


class TestClass(TestCase):

    @opensearchmock
    def test_should_return_something_from_opensearch(self):
        self.assertIsNotNone(some_function_that_uses_opensearch())
```

### Custom Behaviours

You can also force the behaviour of the Opensearch instance by importing the `opensearchmock.behaviour` module:

```python
from unittest import TestCase

from opensearchmock import behaviour


class TestClass(TestCase):

    ...

    def test_should_return_internal_server_error_when_simulate_server_error_is_true(self):
        behaviour.server_failure.enable()
        ...
        behaviour.server_failure.disable()
```

You can also disable all behaviours by calling `behaviour.disable_all()` (Consider put this in your `def tearDown(self)` method)

#### Available Behaviours

* `server_failure`: Will make all calls to Opensearch returns the following error message:
    ```python
    {
        'status_code': 500,
        'error': 'Internal Server Error'
    }
    ```

## Code example

Let's say you have a prod code snippet like this one:

```python
import opensearchpy

class FooService:

    def __init__(self):
        self.es = opensearchpy.OpenSearch(hosts=[{'host': 'localhost', 'port': 9200}])

    def create(self, index, body):
        es_object = self.es.index(index, body)
        return es_object.get('_id')

    def read(self, index, id):
        es_object = self.es.get(index, id)
        return es_object.get('_source')

```

Than you should be able to test this class by mocking ElasticSearch using the following test class:

```python
from unittest import TestCase
from opensearchmock import opensearchmock
from foo.bar import FooService

class FooServiceTest(TestCase):

    @opensearchmock
    def should_create_and_read_object(self):
        # Variables used to test
        index = 'test-index'
        expected_document = {
            'foo': 'bar'
        }

        # Instantiate service
        service = FooService()

        # Index document on OpenSearch
        id = service.create(index, expected_document)
        self.assertIsNotNone(id)

        # Retrive dpcument from OpenSearch
        document = service.read(index, id)
        self.assertEquals(expected_document, document)

```

## Notes:

- The mocked **search** method returns **all available documents** indexed on the index with the requested document type.
- The mocked **suggest** method returns the exactly suggestions dictionary passed as body serialized in Openearch.suggest response. **Atention:** If the term is an *int*, the suggestion will be ```python term + 1```. If not, the suggestion will be formatted as ```python {0}_suggestion.format(term) ```.
Example:
	- **Suggestion Body**:
	```python
    suggestion_body = {
        'suggestion-string': {
            'text': 'test_text',
            'term': {
                'field': 'string'
            }
        },
        'suggestion-id': {
            'text': 1234567,
            'term': {
                'field': 'id'
            }
        }
    }
    ```
    - **Suggestion Response**:
    ```python
    {
        'suggestion-string': [
            {
                'text': 'test_text',
                'length': 1,
                'options': [
                    {
                        'text': 'test_text_suggestion',
                        'freq': 1,
                        'score': 1.0
                    }
                ],
                'offset': 0
            }
        ],
        'suggestion-id': [
            {
                'text': 1234567,
                'length': 1,
                'options': [
                    {
                        'text': 1234568,
                        'freq': 1,
                        'score': 1.0
                    }
                ],
                'offset': 0
            }
        ],
    }
    ```

## Testing

```bash
python setup.py test
```
