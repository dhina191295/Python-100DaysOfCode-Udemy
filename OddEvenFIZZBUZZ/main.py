number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
        print("Fizz")
  elif number % 5 == 0:
        print("Buzz")
  else:
        print(number)
