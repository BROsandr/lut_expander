import unittest
import lut
import numpy
import itertools
import operator

bits2num = lambda bits: int(''.join(str(int(bit)) for bit in bits), base=2)

class TestLut(unittest.TestCase):
  def lut_args2num_wrapper(self, num_of_args: int):
    args = ', '.join(chr(arg + ord('a')) for arg in range(num_of_args))
    def lut_args2num(*args: bool):
      self.assertEqual(len(args), num_of_args, "The lut must contain only two rows 1'b0 and 1'b1.")
      return bits2num(args)
    def lut_2_args(a: bool, b: bool): return lut_args2num(a, b)
    def lut_1_args(a: bool): return lut_args2num(a)
    return lut_1_args

  def test_lut_2(self):
    lut_obj = list(lut.Lut(self.lut_args2num_wrapper(1), lut.Lut_row_format()))
    self.assertEqual(len(lut_obj), 2, "The lut must contain only two rows 1'b0 and 1'b1.")
    self.assertEqual(lut_obj[0].eval_func(), 0)
    self.assertEqual(lut_obj[1].eval_func(), 1)
    self.assertEqual(int(lut_obj[0]), 0)
    self.assertEqual(int(lut_obj[1]), 1)
    self.assertEqual(str(lut_obj[0]), "1'b0: 0")
    self.assertEqual(str(lut_obj[1]), "1'b1: 1")

if __name__ == '__main__':
  unittest.main()
