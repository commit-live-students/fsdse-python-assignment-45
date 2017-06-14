from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath = './files/testfile.txt'
        res = solution(fpath)

        self.assertEqual(res, 5)