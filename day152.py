"""
Day 152: Inheritance: Animals

Question:
Demonstrate inheritance and method overriding with Animal, Dog and Cat.
"""

# Solution
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

for a in (Dog("Bruno"), Cat("Kitty"), Animal("Generic")):
    print(a.name, "says", a.speak())
