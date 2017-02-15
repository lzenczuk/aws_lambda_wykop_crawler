from app import generate_pages_range_handler

import unittest


class GeneratePagesRangeHandlerTestSuit(unittest.TestCase):
    def test_no_parameters(self):
        event = {}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 2
        assert 'Missing to parameter.' in result['errors']
        assert 'Missing from parameter.' in result['errors']

    def test_missing_from_parameter(self):
        event = {'to': 10}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Missing from parameter.' in result['errors']

    def test_missing_to_parameter(self):
        event = {'from': 10}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Missing to parameter.' in result['errors']

    def test_to_parameter_not_a_number(self):
        event = {'from': 10, 'to': 'a'}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Expected to parameter as number, was a' in result['errors']

    def test_from_parameter_not_a_number(self):
        event = {'from': '1b', 'to': 10}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Expected form parameter as number, was 1b' in result['errors']

    def test_to_parameter_smaller_then_0(self):
        event = {'from': 10, 'to': -1}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Expected to parameter bigger then 0, was -1' in result['errors']

    def test_from_parameter_smaller_then_0(self):
        event = {'from': -10, 'to': 11}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Expected form parameter bigger then 0, was -10' in result['errors']

    def test_to_smaller_then_from(self):
        event = {'from': 100, 'to': 80}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'errors' in result
        assert len(result['errors']) == 1
        assert 'Expected to parameter bigger or equal from parameter, was from:  100 to: 80' in result['errors']

    def test_happy_path(self):
        event = {'from': 80, 'to': 100}
        context = {}

        result = generate_pages_range_handler(event, context)
        assert 'from' in result
        assert 'to' in result
        assert result['from']==80
        assert result['to']==100
