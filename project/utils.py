from . import myexception
from enum import Enum

Radix = Enum('Radix', ['DEC', 'BIN', 'HEX', 'OCT'])

def to_verilog_literal(number: int, width: int, radix: Radix)->str:
  if width  <= 0: raise myexception.MyValueError("Number's width should a positive number.")
  if number <  0: raise myexception.MyValueError("Negative literals are not supported.")

  result = str(width)
  if radix == Radix.BIN: return result + "'b" + format(number, f"0{width}b")
  if radix == Radix.DEC: return result + "'d" + format(number, f"d")
  if radix == Radix.HEX: return result + "'h" + format(number, f"x")
  if radix == Radix.OCT: return result + "'o" + format(number, f"o")
