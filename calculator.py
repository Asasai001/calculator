def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b if b != 0 else "Division by zero are not allowed"

def power(a, b):
  return a**b

def sqrt(a):
  return a ** 0.5

def percentage(a):
  return a / 100


def calculator():
  operations = history_load()
  while True:
    while True:
      input_1 = input("Enter your numbers (1): ")
      if '%' in input_1:
        try:
          number = float(input_1.replace('%', ''))
          number_1 = percentage(number)
          break
        except ValueError:
          print(f"Your input {input_1} is not valid. Please try again")
      elif 'v' in input_1[-1]:
        try:
          number = float(input_1.replace('v', ''))
          number_1 = sqrt(number)
          break
        except ValueError:
          print(f"Your input {input_1} is not valid. Please try again")
      else:
        try:
          number_1 = float(input_1)
          break
        except:
          print(f"Your input {input_1} is not valid. Please try again")

    while True:
      input_2 = input("Enter your numbers (2): ")
      if '%' in input_2:
        try:
          number = float(input_2.replace('%', ''))
          number_2 = percentage(number)
          break
        except ValueError:
          print(f"Your input {input_2} is not valid. Please try again")

      elif 'v' in input_2[-1]:
        try:
          number = float(input_2.replace('v', ''))
          number_2 = sqrt(number)
          break
        except ValueError:
          print(f"Your input {input_2} is not valid. Please try again")
      else:
        try:
          number_2 = float(input_2)
          break
        except:
          print(f"Your input {input_2} is not valid. Please try again")

    action = input("Enter mathematical operation (+, -, *, / or **), press q to quit: ")
    if action == 'q':
      history_save(operations)
      break

    result = None
    if action == '+':
      result = add(number_1, number_2)

    elif action == '-':
      result = subtract(number_1, number_2)

    elif action == '*':
      result = multiply(number_1, number_2)

    elif action == '/':
      result = divide(number_1, number_2)

    elif action == '**':
      result = power(number_1, number_2)

    entry = f"{number_1} {action} {number_2} = {result}"
    operations.append(entry)
    history_save(operations)

    print(f"Your latest output: {entry}")
    print(f"History: {operations}")


calculator()