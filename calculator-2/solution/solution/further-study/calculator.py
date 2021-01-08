"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def my_reduce(func, items):
    result = func(items[0], items[1])

    for item in items[2:]:
        result = (func(result, item))

    return result


while True:
    try:
        user_input = input('Enter your equation > ')
    except EOFError:
        print('End of file! Goodbye~')
        break

    tokens = user_input.split(' ')

    if 'q' in tokens:
        print('You will exit.')
        break

    operator, *num_tokens = tokens

    # We have to cast each value we pass to an arithmetic function from a
    # a string into a numeric type. If we use float across the board, all
    # results will have decimal points, so let's do that for consistency.
    nums = []
    try:
        for num in num_tokens:
            nums.append(float(num))
    except ValueError:
        print('Error: one or more of your operands was not a number')
        continue

    # Make sure user enteres correct amount of operands
    if (
        (operator not in ['square', 'cube'] and len(nums) < 2) or
        (operator == 'x+' and len(nums) < 3)
    ):
        print('Error: you did not enter enough operands')
        continue

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    if operator == '+':
        result = my_reduce(add, nums)

    elif operator == '-':
        result = my_reduce(subtract, nums)

    elif operator == '*':
        result = my_reduce(multiply, nums)

    elif operator == '/':
        result = my_reduce(divide, nums)

    elif operator == 'square':
        result = square(nums[0])

    elif operator == 'cube':
        result = cube(nums[0])

    elif operator == 'pow':
        result = my_reduce(power, nums)

    elif operator == 'mod':
        result = my_reduce(mod, nums)

    else:
        print('Error: you gave an invalid operator. Try again.')

    print(result)
