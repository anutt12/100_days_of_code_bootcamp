# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# # greet_with("Jack Bauer", "Nowhere")
# greet_with(location="Nowhere", name="Jack Bauer")

def calculate_love_score(name1, name2):
    keywords = ["true", "love"]

    names = [n.replace(" ", "").lower() for n in [name1, name2]]

    results = []
    for word in keywords:
        total = 0
        for name in names:
            for letter in name:
                total += word.count(letter)
        results.append(str(total))

    print("".join(results))


calculate_love_score("Angela Yu", "Jack Bauer")
