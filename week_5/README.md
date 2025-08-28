# Week 5 OOP Python Assignment 🐍

This folder contains my solutions for the Week 5 OOP assignment, focusing on **encapsulation, inheritance, and polymorphism** in Python.

---

## 📚 Assignment Description

### Activity 1: Design Your Own Class 🏗️
- Implemented a `Smartphone` class with attributes:
  - Brand, Model, Storage, Battery Capacity, Battery Level, Power State.
- Encapsulated attributes using **protected variables** (with getter methods for access).
- Added methods for:
  - Powering on/off.
  - Making calls.
  - Using apps (with battery drain).
  - Charging the device.
  - Retrieving storage and device info.
- Created a subclass `GamingSmartphone` with:
  - Extra attributes (`gpu_model`, `cooling_system`).
  - Methods for gaming features (`enable_gaming_mode`, `play_game`).
  - Demonstrates **inheritance**, **encapsulation**, and **polymorphism**.

### Activity 2: Polymorphism Challenge 🎭
- Implemented a base `Animal` class with methods:
  - `move()`, `speak()`, and `describe()` (enforced with `NotImplementedError`).
- Created subclasses with their own unique implementations:
  - `Bird` → flies, chirps, and has wingspan.
  - `Fish` → swims, glubs, and has fins.
  - `Mammal` → walks, growls, and has legs.
  - `Snake` → slithers, hisses, and has length.
- Demonstrated **polymorphism**: each subclass overrides `move()` and `speak()` differently.

---

## 📂 File Structure

```
week_5/
│-- smartphone.py    # Activity 1: Smartphone & GamingSmartphone
│-- animals.py       # Activity 2: Animal classes with polymorphism
│-- README.md        # Assignment documentation
```

---

## ▶️ How to Run

1. Clone this repository or download the files.
2. Open a terminal in the `week_5` directory.
3. Run the files:

```bash
# Run Activity 1
python smartphone.py

# Run Activity 2
python animals.py
```

---

## ✅ Sample Output

### Activity 1: Smartphone

```
=== Activity 1: Smartphone Class with Inheritance ===

Apple iPhone 15 is now powered on. Battery: 100%
Calling 555-1234... Battery remaining: 98%
Used Instagram for 30 minutes. Battery remaining: 83.0%
Charged for 20 minutes. Battery level: 99.0%
128GB storage
Apple iPhone 15 is now powered off.

==================================================

ASUS ROG Phone 7 is now powered on. Battery: 100%
Gaming mode enabled. Performance boosted!
Played Genshin Impact for 45 minutes with gaming mode. Battery remaining: 46.0%
GPU: Adreno 740, Cooling: Vapor Chamber Cooling
512GB storage
ASUS ROG Phone 7 is now powered off.
```

### Activity 2: Animals (Polymorphism)

```
=== Activity 2: Polymorphism Challenge with Animals ===

Eagle:
  I am a Eagle and I live in Mountains. I have a wingspan of 200cm.
  Movement: 🦅 Flying through the air!
  Sound: 🐦 Chirp chirp!

Clownfish:
  I am a Clownfish and I live in Coral Reef. I have 7 fins.
  Movement: 🐠 Swimming through the water!
  Sound: 🐟 Glub glub!

Lion:
  I am a Lion and I live in Savannah. I have 4 legs.
  Movement: 🐘 Walking on the land!
  Sound: 🐒 Grrr!

Python:
  I am a Python and I live in Jungle. I am 5m long.
  Movement: 🐍 Slithering on the ground!
  Sound: 🐍 Hiss hiss!
```

---

## 🔗 Submission

All assignment solutions are included in this repository.
Run the Python files as shown above to see the demonstrations of **encapsulation, inheritance, and polymorphism** in action.

---

## 🎯 Learning Objectives Achieved

- Implemented classes with proper encapsulation techniques
- Demonstrated inheritance through subclass relationships
- Showcased polymorphism with method overriding
- Practiced constructor implementation for object initialization

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming principles