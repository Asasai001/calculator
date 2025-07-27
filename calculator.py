def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b if b != 0 else "Division by zero are not allowed"

def calculator():
  operations = []
  while True:
    while True:
      try:
        number_1 = float(input("Enter your numbers (1): "))
        break
      except ValueError:
        print(f"Your input {number_1} is not valid. Please try again")

    while True:
      try:
        number_2 = float(input("Enter your numbers (2): "))
        break
      except ValueError:
        print(f"Your input {number_2} is not valid. Please try again")



    action = input("Enter mathematical operation (+, -, * or /), press q to quit: ")
    if action == 'q':
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

    entry = f"{number_1} {action} {number_2} = {result}"
    operations.append(entry)

    print(f"Your latest output: {entry}")
    print(f"History: {operations}")


calculator()