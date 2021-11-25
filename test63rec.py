import unittest
import atp63rec as code

class TestProgramm(unittest.TestCase):
    def test_high_and_low_number(self):
        p = code.create(10,p = [])
        list_a = []
        for n in p:
            if n % 2 == 0:
                list_a.append(n)
            else:
                None
        list_double = code.search_double(p,list_double=[])

        self.assertEqual(list_a, list_double)
