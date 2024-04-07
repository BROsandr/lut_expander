import myexception
import typing

lut_number_of_inputs_exc = lambda number_of_inputs: myexception.MyValueError(f"Lut's number of inputs must be a positive number. number_of_inputs={number_of_inputs}.")

def get_number_of_args(func: typing.Callable)->int:
  from inspect import signature
  return len(signature(func).parameters)

class Lut_row:
  def __init__(self, row_number: int, row_func: typing.Callable):
    number_of_inputs: int = get_number_of_args(row_func)
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    if not(0 <= row_number <= (2**number_of_inputs - 1)): raise myexception.MyValueError(f"Lut's row number must not inside a range [0; number_of_inputs-1]. row_number={row_number}.")
    self.__row_number = row_number
    self.__row_func = row_func

  def __repr__(self):
    return format(self.__row_number, f"0{self._number_of_inputs}b")

class Lut:
  def __init__(self, lut_row_func: typing.Callable):
    self.__lut_row_func = lut_row_func
    number_of_inputs = get_number_of_args(lut_row_func)
    if number_of_inputs <= 0: raise lut_number_of_inputs_exc(number_of_inputs)
    self.__current_row = None
    self.__iter_num: int = 0

  def __iter__(self):
    return self

  def __next__(self)->Lut_row:
    if self.__iter_num == get_number_of_args(self.__lut_row_func): raise StopIteration
    next_row = self._get_next_row(self.__current_row)
    self.__iter_num += 1
    self.__current_row = next_row
    return Lut_row(next_row, self.__lut_row_func)

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
