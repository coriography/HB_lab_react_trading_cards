"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_input = input('Enter your equation > ')
    tokens = user_input.split(' ')

    if 'q' in tokens:
        print('You will exit.')
        break

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) == 3:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    # We have to cast each value we pass to an arithmetic function from a
    # a string into a numeric type. If we use float across the board, all
    # results will have decimal points, so let's do that for consistency.

    if operator == '+':
        result = add(float(num1), float(num2))

    elif operator == '-':
        result = subtract(float(num1), float(num2))

    elif operator == '*':
        result = multiply(float(num1), float(num2))

    elif operator == '/':
        result = divide(float(num1), float(num2))

    elif operator == 'square':
        result = square(float(num1))

    elif operator == 'cube':
        result = cube(float(num1))

    elif operator == 'pow':
        result = power(float(num1), float(num2))

    elif operator == 'mod':
        result = mod(float(num1), float(num2))

    print(result)
