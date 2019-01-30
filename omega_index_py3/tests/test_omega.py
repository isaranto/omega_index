# -*- coding: utf-8 -*-
from omega_index_py3 import Omega
import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_node_assignment(self):
        comms = {0: [1, 2, 3], 1: [3, 4, 5]}
        self.assertEqual(Omega(comms, comms).get_node_assignment(comms),
                         {1: [0], 2: [0], 3: [0, 1], 4: [1], 5: [1]})

    def test_common_clusters(self):
        comms = {0: [1, 2, 3], 1: [3, 4, 5]}
        nodes_dict = {1: [0, 1, 2], 2: [0, 1], 3: [0, 1], 4: [1], 5: [1]}
        self.assertEqual(Omega(comms, comms).num_of_common_clusters(1, 2, nodes_dict), 2)


if __name__ == '__main__':
    unittest.main()
