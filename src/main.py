from utils import square, is_even, celsius_to_fahrenheit


number = float(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("Even or odd: Even")
else:
    print("Even or odd: Odd")

print("Fahrenheit:", celsius_to_fahrenheit(number))