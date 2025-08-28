class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
        
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def describe(self):
        return f"I am a {self.name} and I live in {self.habitat}."


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan  # in cm
        
    def move(self):
        return "🦅 Flying through the air!"
    
    def speak(self):
        return "🐦 Chirp chirp!"
    
    def describe(self):
        return f"{super().describe()} I have a wingspan of {self.wingspan}cm."


class Fish(Animal):
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
        
    def move(self):
        return "🐠 Swimming through the water!"
    
    def speak(self):
        return "🐟 Glub glub!"
    
    def describe(self):
        return f"{super().describe()} I have {self.fin_count} fins."


class Mammal(Animal):
    def __init__(self, name, habitat, leg_count):
        super().__init__(name, habitat)
        self.leg_count = leg_count
        
    def move(self):
        return "🐘 Walking on the land!"
    
    def speak(self):
        return "🐒 Grrr!"
    
    def describe(self):
        return f"{super().describe()} I have {self.leg_count} legs."


class Snake(Animal):
    def __init__(self, name, habitat, length):
        super().__init__(name, habitat)
        self.length = length  # in meters
        
    def move(self):
        return "🐍 Slithering on the ground!"
    
    def speak(self):
        return "🐍 Hiss hiss!"
    
    def describe(self):
        return f"{super().describe()} I am {self.length}m long."


# Demonstration
if __name__ == "__main__":
    print("=== Activity 2: Polymorphism Challenge with Animals ===\n")
    
    # Create animals of different types
    animals = [
        Bird("Eagle", "Mountains", 200),
        Fish("Clownfish", "Coral Reef", 7),
        Mammal("Lion", "Savannah", 4),
        Snake("Python", "Jungle", 5)
    ]
    
    # Demonstrate polymorphism
    for animal in animals:
        print(f"{animal.name}:")
        print(f"  {animal.describe()}")
        print(f"  Movement: {animal.move()}")
        print(f"  Sound: {animal.speak()}")
        print()