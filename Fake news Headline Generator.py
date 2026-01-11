import random 
subjects = [
    "Virat Kohli",
    "Sachin Tendulkar",
    "MS Dhoni",
    "A Mumbai ca",
    "Prime Minister",
    "Auto Rickshaw",
]
actions = [
    "launched",
    "cancels",
    "dances with",
    "easts",
    "declares war on",
    "spots ",
]
place_or_things = [
    "AT Red Fort",
    "the Parliament",
    "the Supreme Court",
    "the National Stadium",
    "the Central Railway Station",
    "the Mumbai Airport",
]
while True:
    subjects =random.choice(subjects)
    actions =random.choice(actions)
    place_or_things =random.choice(place_or_things)
    headline = f"BREAKING NEWS: {subjects} {actions} {place_or_things}!"
    print("\n" + headline)
    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        print("Thank you for using the Fake News headline Generator. Goodbye!")
        break
print("Thank you for usig the fake headline generator. Goodbye!")

