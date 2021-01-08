"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator():
    while True:
        try:
            read_input = input("Enter your equation: ")
            tokens = read_input.split(" ")

            if "q" in tokens:
                print("Quit")
                break

            else:
                if tokens[0] == "+":  
                    answer = add(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "-":
                    answer = subtract(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "*":
                    answer = multiply(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "/":
                    answer = divide(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "square":
                    answer = square(float(tokens[1]))
                    print(answer)
                elif tokens[0] == "cube":
                    answer = cube(float(tokens[1]))
                    print(answer)
                elif tokens[0] == "pow":
                    answer = power(float(tokens[1]), float(tokens[2]))
                    print(answer)
                elif tokens[0] == "mod":
                    answer = mod(float(tokens[1]), float(tokens[2]))
                    print(answer)
                else:
                    print("Please type in an operator and 2 numbers separated by spaces.")
        except ValueError:
            print('That is not a number.')
calculator()