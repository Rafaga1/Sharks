import unittest

from make_tree import add_url


class TestStringMethods(unittest.TestCase):

    def test_exist_key(self):
        result = add_url([("GET", "/api/v1/cluster/metrics"),
                          ("POST", "/api/v1/cluster/{cluster}/plugins"),
                          ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}")])
        self.assertIn(result['cluster']['metrics'], 'GET')
        # self.assertIn('metrics', result['cluster'])

    def test_not_exist_key(self):
        result = add_url([("GET", "/api/v1/cluster/freenodes/list"),
                          ("GET", "/api/v1/cluster/nodes"),
                          ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                          ("POST", "/api/v1/cluster/{cluster}/plugins")])
        self.assertNotIn('cluster', result['cluster'])
