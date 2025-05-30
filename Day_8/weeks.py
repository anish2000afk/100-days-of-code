def life_in_weeks(age):
    left_years = 90 - age
    weeks_in_life = left_years * 52
    print(f"You have {weeks_in_life} weeks left.")


def greet_with(name="Anish", location="Bristol"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with()
