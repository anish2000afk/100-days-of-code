"""This one works with while loops only"""

import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)

    while True:  # Outer loop: Keeps running for new calculations
        num1 = float(input("What is the first number?: "))
        should_continue = True

        while should_continue:  # Inner loop: Keeps running current chain
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' to quit: "
            )

            if choice == "y":
                num1 = answer
            elif choice == "n":
                print("\n" * 20)
                should_continue = False
                print(art.logo)
            elif choice == "exit":
                print("Goodbye!")
                return
            else:
                print("Invalid input. Exiting.")
                return


calculator()
