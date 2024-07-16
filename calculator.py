# ANSI escape sequences for colors
class colors:
   WELCOME = '\033[92m'  # Green
   OPTION = '\033[94m'  # Blue
   INPUT_PROMPT = '\033[96m'  # Cyan
   FIRST_NUMBER = '\033[95m'  # Magenta
   SECOND_NUMBER = '\033[91m'  # Red
   ANSWER = '\033[93m'  # Yellow
   NEXT_CALC = '\033[90m'  # Grey
   END = '\033[0m'  # End of color

def add(x, y):
    return x + y

def sub(x, y):
   return x - y

def mul(x, y):
   return x * y

def div(x, y):
   return x / y

def sqrt(x):
   return x ** 0.5

def percentage(x, y):
   return (x / y) * 100

def is_valid_input(input_str):
   return input_str.isalpha()

print(f"{colors.WELCOME}Welcome to my Calculator{colors.END}")
print(f"{colors.OPTION}1. Add{colors.END}")
print(f"{colors.OPTION}2. Subtraction{colors.END}")
print(f"{colors.OPTION}3. Multiplication{colors.END}")
print(f"{colors.OPTION}4. Division{colors.END}")
print(f"{colors.OPTION}5. Square Root{colors.END}")
print(f"{colors.OPTION}6. Percentage{colors.END}")

while True:
   choice = input(f"{colors.INPUT_PROMPT}Enter your option (1/2/3/4/5/6): {colors.END}")
   if choice in ('1', '2', '3', '4', '5', '6'):
      try:
         if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input(f"{colors.FIRST_NUMBER}Enter first number: {colors.END}"))
            num2 = float(input(f"{colors.SECOND_NUMBER}Enter second number: {colors.END}")) if choice != '5' else 0
         else:
            num1 = float(input(f"{colors.FIRST_NUMBER}Enter the number: {colors.END}"))
      except ValueError:
         print("Invalid input. Please enter a number.")
         continue
      
      if choice == '1':
         print(f"{colors.ANSWER}{num1} + {num2} = {add(num1, num2)}{colors.END}")
      elif choice == '2':
         print(f"{colors.ANSWER}{num1} - {num2} = {sub(num1, num2)}{colors.END}")
      elif choice == '3':
         print(f"{colors.ANSWER}{num1} * {num2} = {mul(num1, num2)}{colors.END}")
      elif choice == '4':
         print(f"{colors.ANSWER}{num1} / {num2} = {div(num1, num2)}{colors.END}")
      elif choice == '5':
         print(f"{colors.ANSWER}√{num1} = {sqrt(num1)}{colors.END}")
      elif choice == '6':
         print(f"{colors.ANSWER}{num1} is {percentage(num1, num2)}% of {num2}{colors.END}")

      while True:
         next_calculation = input(f"{colors.NEXT_CALC}Let's do next calculation? (yes/no): {colors.END}")
         if is_valid_input(next_calculation) and next_calculation.lower() in ('yes', 'no'):
            break
         else:
            print("Invalid input. Please enter 'yes' or 'no'.")
      
      if next_calculation.lower() == "no":
         break
   else:
      print("Invalid option. Please choose a valid option from 1 to 6.")

print(f"{colors.WELCOME}Thanks for using the calculator!{colors.END}")
