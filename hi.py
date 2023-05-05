try:
    # code that may raise an exception
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    # handle the ZeroDivisionError exception
    print("Cannot divide by zero.")
else:
    print("The result is:", y)
finally:
    print("End of program.")

try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")
