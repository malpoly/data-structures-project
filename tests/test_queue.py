import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    """тесты с использованием unittest для модуля queue """
    def test_enqueue(self):
        test_queue = Queue()
        test_queue.enqueue("1")
        test_queue.enqueue("2")
        test_queue.enqueue("3")
        self.assertEqual(test_queue.head.data, "1")
        self.assertEqual(test_queue.tail.data, "3")


    def test_dequeu(self):
        test_queue = Queue()
        test_queue.enqueue("1")
        test_queue.enqueue("2")
        test_queue.enqueue("3")
        self.assertEqual(test_queue.head.data, "1")
        test_queue.dequeue()
        self.assertEqual(test_queue.head.data, "2")
        test_queue.dequeue()
        self.assertEqual(test_queue.head.data, "3")
        test_queue.dequeue()
        self.assertEqual(test_queue.head, None)

    def test_str(self):
        test_queue = Queue()
        test_queue.enqueue("1")
        test_queue.enqueue("2")
        test_queue.enqueue("3")
        self.assertEqual(str(test_queue), "1\n2\n3")



