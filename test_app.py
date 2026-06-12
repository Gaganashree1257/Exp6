from app import add


def assert_add_positive():
  assert add(2,3) == 5


def assert_add_negative():
  assert add(-1,-1) == -2



def assert_add_zero():
  assert add(0,5) == 5


def assert_add_mixed():
  assert add(-2,-2) == 0


def assert_output_type():
  result = add(10,5)
  assert isinstance (result,int)
  assert result == 15

  
