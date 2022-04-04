zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:

    for i in zoo:
        z = str(zoo)
        f.write(z)
    f.write(str(number))


