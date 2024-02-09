def conversion(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temp = float(input("Enter a temperature in Fahrenheit: "))
celsius_temp = conversion(fahrenheit_temp)
print("Equivalent temperature in Celsius:", celsius_temp)
