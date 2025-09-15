from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of two numbers: a - b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return the quotient a / b."""
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def _read_number(prompt: str) -> Number:
    """Prompt until a valid number is provided."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def _read_operator() -> str:
    """Prompt until a valid operator is chosen."""
    available = " ".join(OPERATIONS.keys())
    while True:
        op = input(f"Pick an operation ({available}): ").strip()
        if op in OPERATIONS:
            return op
        print("Please choose a valid operator.")


def calculator() -> None:
    """Interactive calculator with chaining and reset."""
    from art import logo  # Add the logo from art.py
    while True:
        # Start a fresh session and wipe previous results
        print(logo)
        current = _read_number("What's the first number?: ")

        while True:
            op = _read_operator()
            b = _read_number("What's the next number?: ")

            if op == "/" and b == 0:
                print("Cannot divide by zero. Please enter a non-zero number.")
                continue

            result = OPERATIONS[op](current, b)
            print(f"{current} {op} {b} = {result}")

            choice = input(
                f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'x' to exit: "
            ).strip().lower()

            if choice == "y":
                current = result
            elif choice == "x":
                return
            else:
                # Break to outer loop to start a new calculation and wipe memory
                break


if __name__ == "__main__":
    calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))
