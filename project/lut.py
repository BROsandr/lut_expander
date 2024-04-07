import myexception
import typing

lut_number_of_inputs_exc = lambda number_of_inputs: myexception.MyValueError(f"Lut's number of inputs must be a positive number. number_of_inputs={number_of_inputs}.")

def get_number_of_args(func: typing.Callable)->int:
  from inspect import signature
  return len(signature(func).parameters)

class Lut_row:
  def __init__(self, row_number: int, number_of_inputs: int):
    if row_number < 0: raise myexception.MyValueError(f"Lut's row number must not be a negative number. row_number={row_number}.")
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    self.__row_number = row_number
    self._number_of_inputs = number_of_inputs

  def __repr__(self):
    return format(self.__row_number, f"0{self._number_of_inputs}b")

class Lut:
  def __init__(self, number_of_inputs: int):
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    self._number_of_inputs = number_of_inputs
    self.__current_row = None
    self.__iter_num: int = 0

  def __iter__(self):
    return self

  def __next__(self)->Lut_row:
    if self.__iter_num == self._number_of_inputs: raise StopIteration
    next_row = self._get_next_row(self.__current_row)
    self.__iter_num += 1
    self.__current_row = next_row
    return Lut_row(next_row, self._number_of_inputs)

  def _get_next_row(self, current_row)->int:
    return 0 if current_row is None else current_row + 1

if __name__ == "__main__":
  Lut(3)
  try:
    Lut(-1)
  except myexception.MyException as err:
    ...
  try:
    Lut(-1)
  except ValueError as err:
    print(err)
