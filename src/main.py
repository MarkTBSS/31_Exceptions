a = '1'
b = '#'

try:
    intA = int(a)
    intB = int(b)
    result = intA / intB
except ZeroDivisionError as err:
    print("Error Code: integer division or modulo by zero")
except ValueError as err:
    print("ValueError: Error Code:", err)
else:
    print(result)