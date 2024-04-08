import abc
from .utils import *

class Lut_row_format(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def __call__(self, row_number: int, number_of_inputs: int, row_func_output)->str:
    ...

class Lut_row_verilog_format(Lut_row_format):
  def __init__(self, case_literal_radix: Radix = Radix.BIN):
    self._case_literal_radix = case_literal_radix

  def __call__(self, row_number: int, number_of_inputs: int, row_func_output)->str:
    return to_verilog_literal(number=row_number, width=number_of_inputs, radix=self._case_literal_radix) + ': ' + str(row_func_output) + ';'

class Lut_row_rand_radix_format(Lut_row_verilog_format):
  def __init__(self):
    import random
    super().__init__(random.choice(list(Radix)))
