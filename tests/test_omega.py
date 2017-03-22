# -*- coding: utf-8 -*-
import unittest

from context import omega_index
import unittest

comms1 = {1: [5, 6, 7], 2: [3, 4, 5], 3: [6, 7, 8]}
comms2 = {1: [5, 6, 7], 2: [3, 4, 6], 3: [6, 7, 8]}
comms3 = {1: [5, 6, 7], 2: [6, 7, 8], 3: [3, 4, 5]}
comms4 = {0: ['1-t0', '2-t0', '3-t0', '4-t0', '1-t1', '2-t1',  '3-t1','4-t1', '1-t2','2-t2','3-t2','4-t2'],
          1: ['11-t1', '12-t1', '13-t1'],
          2: ['5-t2', '6-t2', '7-t2', '5-t0', '6-t0', '7-t0']}
comms5 = {1: ['11-t1', '12-t1', '13-t1'],
          2: ['1-t0', '2-t0', '3-t0', '4-t0', '1-t1', '2-t1',  '3-t1','4-t1', '1-t2','2-t2','3-t2','4-t2'],
          3: ['5-t2', '6-t2', '7-t2', '5-t0', '6-t0', '7-t0']}

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_node_assignment(self):
        comms = {0: [1, 2, 3], 1: [3, 4, 5]}
        self.assertEqual(omega_index.Omega(comms, comms).get_node_assignment(comms), {1:[0], 2:[0], 3:[0,1], 4:[1],
                                                                                    5:[1]})
    def test_common_clusters(self):
        comms = {0: [1, 2, 3], 1: [3, 4, 5]}
        nodes_dict = {1:[0, 1, 2], 2:[0, 1], 3: [0, 1], 4: [1], 5: [1] }
        self.assertEqual(omega_index.Omega(comms, comms).num_of_common_clusters(1,2, nodes_dict), 2)

if __name__ == '__main__':
    unittest.main()



# omega = omega_index.Omega(comms4, comms5)
# print omega.omega_score
