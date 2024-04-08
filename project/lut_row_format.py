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

class Lut_row_format_factory(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get_format(self, number: int)->Lut_row_format:
    ...

class Lut_row_format_factory_same(Lut_row_format_factory):
  def __init__(self, lut_row_format: Lut_row_format):
    self.format = lut_row_format

  def get_format(self, number: int)->Lut_row_format:
    return self.format

class Lut_row_format_factory_rand(Lut_row_format_factory):
  def get_format(self, number: int)->Lut_row_format:
    import random
    return Lut_row_verilog_format(random.choice(list(Radix)))
