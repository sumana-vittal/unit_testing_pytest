import train
import unittest

class TestRouteScore(unittest.TestCase):

    def test_negative_trains_should_return_0_points(self):
        score = train.get_route_score(-2)
        self.assertEqual(score,0)

    def test_0_trains_should_return_0_points(self):
        score = train.get_route_score(0)
        self.assertEqual(score,0)

    def test_2_trains_should_return_2_points(self):
        score = train.get_route_score(2)
        self.assertEqual(score,2)

    def test_3_trains_should_return_4_points(self):
        score = train.get_route_score(3)
        self.assertEqual(score,4)

    def test_4_trains_should_return_7_points(self):
        score = train.get_route_score(4)
        self.assertEqual(score,7)

    def test_5_trains_should_return_double_points(self):
        score = train.get_route_score(5)
        self.assertEqual(score,10)

    def test_25_trains_should_return_double_points(self):
        score = train.get_route_score(25)
        self.assertEqual(score,50)