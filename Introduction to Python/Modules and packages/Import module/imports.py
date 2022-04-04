import my_module
import calculator

my_module.hello_world("John")


calc = calculator.Calculator()
for i in range(100):
    # Use Calculator method `add` to add `i` to the current value.
    calc.add(i)

print(calc.get_current())




