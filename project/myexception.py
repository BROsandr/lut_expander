class MyException(Exception):
  ...

class MyValueError(MyException, ValueError):
  ...