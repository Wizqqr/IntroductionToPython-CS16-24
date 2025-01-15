c = 6
f = c

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

f_converted = convert_fahrenheit_to_celsius(f)
print(f"{f} degrees Fahrenheit is equal to {f_converted:.2f} degrees Celsius")

c_converted = convert_fahrenheit_to_celsius(c)
print(f"{c} degrees Celsius is equal to {c_converted:.2f} degrees Fahrenheit")

def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32




num1 = float(input("Enter the first number: "))
num2 = float(int(input("Enter the second number: ")))
num3 = float(int(input("Enter the third number: ")))
sum = num1 + num2
product = num1 * num2
average = (num1 + num2) / 2
max_num = max(num1, num2)
min_num = min(num1, num2)

print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")

print(f"{num1} * {num2} = {num1 * num2}")

print(f"{num1} + {num2} = {num1 + num2}")

print(f"{num1} - {num2} = {num1 - num2}")

print(f"{num1} / {num2} = {num1 / num2:.2f}")

print(f"{num1} % {num2} = {num1 % num2}")

print(f"{num1} ** {num2} = {num1 ** num2}")

print(f"{num1} // {num2} = {num1 // num2}")




