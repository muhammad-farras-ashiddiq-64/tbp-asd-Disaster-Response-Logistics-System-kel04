import unittest
from src.data_structures.linked_list import LLNode

class TestLinkedListNode(unittest.TestCase):
    def test_node_creation(self):
        """Memastikan node dasar dapat menyimpan data dan pointer dengan benar."""
        node = LLNode("DATA_TES")
        self.assertEqual(node.data, "DATA_TES")
        self.assertIsNone(node.next)

    def test_node_linkage(self):
        """Memastikan rantai penunjukan pointer antar node berfungsi."""
        node1 = LLNode(100)
        node2 = LLNode(200)
        node1.next = node2
        self.assertEqual(node1.next.data, 200)

if __name__ == "__main__":
    unittest.main()
