print("Hello Dhinesh")

##D H I N E S H
##0 1 2 3 4 5 6

name = "Dhinesh Kumar"
fname = "Dhinesh"
lname = "Kumar"
full_name = fname + lname
print(full_name)
full_name = fname + ' ' + lname
print(full_name)
full_name = fname + " " + lname
print(full_name)
print("Hello" ,name)
print("Hello",name ,",Nice to meet you")
str = "hello" + " DHINA"
print(str)

print(name[:])
print(name[::-1])
print(name[::2])
print(name[2::2])
print(name[:4:1])
print(name[2:5:2])


#Numeric Operators

x= 20
print(x)
print("x")
x = x+2
print(x)
y = 21*12
print("y = ",y)

z = y/10 # provides result as float type
print(type(z))
print("y/10 = ",z)

zz = y//10  # provides result as int type instead of float type
print(type(zz))
print("y//10 = ",zz)

zy = y%10
print(type(zy))
print("y%10 = ",zy)

x= 34.5
print(type(x))
print(x)
print(int(x))


x = 9**2
print(x)

##Operator Precedence
##
##Paranthesis
##Power
##Multiplication
##Addition
##Let to Right

#INPUT

name = input("Please enter a name: ")
print("Hi ",name)

value = input("Enter a number: ")
print(type(value))
print(value)

value1 = int(input("Enter a number: "))
print(type(value1))
print(value1)


#IF
x = 0
y= 10
if 0 == x:
    if y == 10:
        print("True")
    else:
        print("False")

