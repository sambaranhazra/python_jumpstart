import unittest

from activities import eat, nap


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Testing for healthy food eat function"""
        self.assertEqual(eat("brocolli", is_healthy=True),
                         "I'm eating brocolli, because my body is a temple.")

    def test_eat_unhealthy(self):
        """Testing for unhealthy food eat function"""
        self.assertEqual(eat("pizza", is_healthy=False), "I'm eating pizza, because YOLO")


if __name__ == '__main__':
    unittest.main()
