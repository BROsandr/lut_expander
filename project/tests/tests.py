import unittest
from .. import lut
from .. import myexception

bits2num = lambda bits: int(''.join(str(int(bit)) for bit in bits), base=2)

class TestLut(unittest.TestCase):
  def lut_args2num_wrapper(self, num_of_args: int):
    def lut_args2num(*args: bool):
      self.assertEqual(len(args), num_of_args, "The lut must contain only two rows 1'b0 and 1'b1.")
      return bits2num(args)
    def lut_2_args(a: bool, b: bool): return lut_args2num(a, b)
    def lut_1_args(a: bool): return lut_args2num(a)

    if num_of_args == 1: return lut_1_args
    if num_of_args == 2: return lut_2_args

    raise myexception.MyValueError(f"Unsupported num_of_args=={num_of_args}.")

  def test_lut_1(self):
    lut_obj = list(lut.Lut(self.lut_args2num_wrapper(1), lut.Lut_row_bin_format()))
    self.assertEqual(len(lut_obj), 2, "The lut must contain only two rows 1'b0 and 1'b1.")
    self.assertEqual(lut_obj[0].eval_func(), 0)
    self.assertEqual(lut_obj[1].eval_func(), 1)
    self.assertEqual(int(lut_obj[0]), 0)
    self.assertEqual(int(lut_obj[1]), 1)
    self.assertEqual(str(lut_obj[0]), "1'b0: 0")
    self.assertEqual(str(lut_obj[1]), "1'b1: 1")
    self.assertEqual(lut_obj, sorted([lut_obj[1], lut_obj[0]]))

  def test_lut_2(self):
    lut_obj = list(lut.Lut(self.lut_args2num_wrapper(2), lut.Lut_row_bin_format()))
    self.assertEqual(len(lut_obj), 4, "The lut must contain only four rows: 2'b00, 2'b01, 2'b10, 2'b11.")
    self.assertEqual(lut_obj[0].eval_func(), 0)
    self.assertEqual(lut_obj[1].eval_func(), 1)
    self.assertEqual(lut_obj[2].eval_func(), 2)
    self.assertEqual(lut_obj[3].eval_func(), 3)
    self.assertEqual(int(lut_obj[0]), 0)
    self.assertEqual(int(lut_obj[1]), 1)
    self.assertEqual(int(lut_obj[2]), 2)
    self.assertEqual(int(lut_obj[3]), 3)
    self.assertEqual(str(lut_obj[0]), "2'b00: 0")
    self.assertEqual(str(lut_obj[1]), "2'b01: 1")
    self.assertEqual(str(lut_obj[2]), "2'b10: 2")
    self.assertEqual(str(lut_obj[3]), "2'b11: 3")

    import random
    _ = list(lut_obj)
    random.shuffle(_)
    assert(lut_obj != _)
    self.assertEqual(lut_obj, sorted(_))

if __name__ == '__main__':
  unittest.main()
