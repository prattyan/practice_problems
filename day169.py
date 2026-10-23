"""
Day 169: Custom Exception

Question:
Define and raise a custom exception for an invalid age.
"""

# Solution
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}")
    return age

for a in (25, -5):
    try:
        print("Age set to", set_age(a))
    except InvalidAgeError as e:
        print("Error:", e)
