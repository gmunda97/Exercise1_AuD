#!/usr/bin/env python3
# Question 1

def name_age():
  name = input("What is your name?")
  age = input("How old are you?")
  print("Hello", name + ". " + "Your age is", age)

  return name+age

name_age()

# Question 2

def swap_integers(num1, num2):
  num1 = str(num1)
  num2 = str(num2)
  num1 += num2
  return int(num1)

num1 = 10
num2 = 22

temp = num1
num1 = num2
num2 = temp

swap_integers(num1, num2)

# Question 4

def check_numbers(num1, num2):
  if num1 % 6 == 0 and num2 % 10 == 0:
    return True
  elif num1 % 10 == 0:
    return True
  else:
    return False

check_numbers(41, 10)

def check_numbers(num1, num2):
  if num1 % 6 ==0 and num2 % 10 == 0:
    return True
  elif num1 % 10 == 0:
    return True
  else:
    return False

check_numbers(60, 10)

# Question 4

def sum_up(num1, num2):
  nums_between = range(num1, num2+1)
  sum_up = 0
  for num in nums_between:
    sum_up += num
  return sum_up


  if num2 > num1:
    return True
  elif num1 and num2 > 0:
    return True
  else:
    return 0

sum_up(3, 9)

# Question 5

def circle_area(r1, r2, r3):
  return PI * (r1 ** 2)
  return PI * (r1 ** 2)
  return PI * (r3 ** 2)

PI = 3.14

circle_area(9, 3, 1)

# Question 6

def check_string(text):
  text = text.lower()
  if text.startswith("a") or text.endswith("a"):
    return True
  else:
    return False

check_string("Antarctic")

# Question 7

def triangle(rows):
  for i in range(rows):
    for j in range(i + 1):
      print("* ", end = "")
    print()

triangle(4)

