def format_name(first_name: str, last_name: str) -> str:
    """Return the full name in the title case without printing."""
    formatted_first = first_name.title()
    formatted_last = last_name.title()
    return f"{formatted_first} {formatted_last}"


print(f"Result: {format_name('anGeLa', 'yu')}")
print(f"Result: {format_name('john', 'doe')}")

# def function_1(text):
#     return text + text
#
# def function_2(text):
#     return text.title()
#
# output = function_2(function_1("hello"))
# print(output)