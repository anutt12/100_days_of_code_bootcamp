ERROR_INVALID_INPUT = "You did not provide valid inputs"


def normalize_name(value: str) -> str:
    """Trim whitespace and convert a name component to title case."""
    return value.strip().title()


def format_full_name(first_name: str, last_name: str) -> str:
    """Return a formatted full name or an error message if inputs are invalid.

    Args:
        first_name: The user's first name.
        last_name: The user's last name.

    Returns:
        A string in the form "Result: First Last" or an error message.
    """
    if not first_name or not last_name or not first_name.strip() or not last_name.strip():
        return ERROR_INVALID_INPUT

    formatted_first = normalize_name(first_name)
    formatted_last = normalize_name(last_name)
    return f"Result: {formatted_first} {formatted_last}"


def main() -> None:
    first = input("What is your first name? ").strip()
    last = input("What is your last name? ").strip()
    print(format_full_name(first, last))


if __name__ == "__main__":
    main()
