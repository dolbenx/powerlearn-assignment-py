# Base class representing a generic Character
class Character:
    def __init__(self, name, alias, superpower):
        self.name = name  # Real name of the character
        self.alias = alias  # Superhero alias (e.g., Spider-Man)
        self.superpower = superpower  # Superpower the character has

    def introduce(self):
        print(f"Hello, I am {self.name}, but you can call me {self.alias}!")

    def use_superpower(self):
        print(f"{self.alias} uses {self.superpower}!")


# Inheriting the Character class to create a Superhero class
class Superhero(Character):
    def __init__(self, name, alias, superpower, sidekick=None):
        super().__init__(name, alias, superpower)  # Inheriting attributes from Character
        self.sidekick = sidekick  # Optional sidekick for the superhero

    # Overriding introduce method to add a twist for superheroes
    def introduce(self):
        super().introduce()
        if self.sidekick:
            print(f"I'm never alone! My sidekick, {self.sidekick}, is with me!")

    # Adding a new method specific to superheroes
    def save_the_day(self, villain):
        print(f"{self.alias} is saving the day by stopping {villain}!")


# Create instances of Superhero and Character
batman = Superhero("Bruce Wayne", "Batman", "Martial arts and gadgets")

batman.introduce()
batman.use_superpower()
batman.save_the_day("The Joker")
