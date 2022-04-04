# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
    print("Hi")
    print("Hello")
    print("Hey")


greet()

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"are you from {location} ?")

greet_with("Dhinesh","Coimbatore")   ## Positional arguments
greet_with("Coimbatore","Dhinesh")

greet_with(name="Dhinesh",location="Coimbatore")    ## keyword Arguments

greet_with(location= "Coimbatore", name = "Dhinesh")
