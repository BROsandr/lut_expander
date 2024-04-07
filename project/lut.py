from __future__ import annotations

import myexception
import typing
import functools

lut_number_of_inputs_exc = lambda number_of_inputs: myexception.MyValueError(f"Lut's number of inputs must be a positive number. number_of_inputs={number_of_inputs}.")

num2args = lambda number: (bool(int(el)) for el in bin(number)[2:])

class Lut_row_format:
  def __call__(self, row_number: int, number_of_inputs: int, row_func_output: str)->str:
    return str(number_of_inputs) + "'b" + format(row_number, f"0{number_of_inputs}b") + ': ' + row_func_output

def get_number_of_args(func: typing.Callable)->int:
  from inspect import signature
  return len(signature(func).parameters)

@functools.total_ordering
class Lut_row:
  def __init__(self, row_number: int, row_func: typing.Callable, row_format: Lut_row_format):
    number_of_inputs: int = get_number_of_args(row_func)
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    if not(0 <= row_number <= (2**number_of_inputs - 1)): raise myexception.MyValueError(f"Lut's row number must not inside a range [0; number_of_inputs-1]. row_number={row_number}, number_of_inputs={number_of_inputs}.")
    self.__row_number = row_number
    self.__row_func = row_func
    self.__row_format = row_format

  def __int__(self):
    return self.__row_number

  def __repr__(self):
    return self.__row_format(row_number=self.__row_number, number_of_inputs=get_number_of_args(self.__row_func), row_func_output=str(self.eval_func()))

  def __eq__(self, other: Lut_row):
    return int(self) == int(other)

  def __lt__(self, other: Lut_row):
    return int(self) < int(other)

  def eval_func(self)->typing.Any:
    return self.__row_func(*num2args(self.__row_number))

class Lut:
  def __init__(self, lut_row_func: typing.Callable, lut_row_format: Lut_row_format):
    self.__lut_row_func = lut_row_func
    number_of_inputs = get_number_of_args(lut_row_func)
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    self.__current_row = None
    self.__iter_num: int = 0
    self.__lut_row_format = lut_row_format

  def __iter__(self):
    return self

  def __next__(self)->Lut_row:
    if self.__iter_num == 2**get_number_of_args(self.__lut_row_func): raise StopIteration
    next_row = self._get_next_row(self.__current_row)
    self.__iter_num += 1
    self.__current_row = next_row
    return Lut_row(row_number=next_row, row_func=self.__lut_row_func, row_format=self.__lut_row_format)

  def _get_next_row(self, current_row)->int:
    return 0 if current_row is None else current_row + 1
