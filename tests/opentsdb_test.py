import unittest
import opentsdb.query

import opentsdb.request

class TestRequestBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.request_builder_valid = opentsdb.request.RequestBuilder()

    def assert_true(self):
        self.assertTrue(True)

class TestQueryBuilder(unittest.TestCase):
    def setUp(self) -> None:
        self.query_builder_valid = opentsdb.query.QueryBuilder()

    def assert_true(self):
        self.assertTrue(True)

class TestRateOptions(unittest.TestCase):
    def setUp(self) -> None:
        self.rate_options_valid = opentsdb.query.RateOptions(counter=False, drop_resets=True, counter_max=100, reset_value=1000)
        self.rate_options_defaults_valid = opentsdb.query.RateOptions(drop_resets=True, reset_value=1000)

    def test_all_values_given(self):
        self.assertTrue(True)

class TestFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.filter_valid = opentsdb.query.Filter(type="wildcard", tagk="tagk", filter="filter", group_by=False)

    def test_all_values_given(self):
        self.assertTrue(True)