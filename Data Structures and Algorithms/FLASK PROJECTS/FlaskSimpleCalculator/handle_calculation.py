# handle_calculation.py

def calculate(operand_1: int, operand_2: int, operator: str) -> int:
  """
  calculation between the operands using the operator and returns a value 

  Parameters:

  -operand_1: the first given value
  -operand_2: the second given value
  -operator: used to trigger the calculation
  """
  if(operand_2 == 0 and operator=='Division'):
    result='Invalid_operation'
  elif(operator == 'Addition'):
    result = operand_1 + operand_2
  elif(operator == 'Subtraction'):
    result = operand_1 - operand_2
  elif(operator == 'Multiplication'):
    result = operand_1 * operand_2
  elif(operator == 'Division'):
    result = operand_1 / operand_2
  else:
    result = 'Invalid_Choice'

  return result
