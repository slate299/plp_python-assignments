# 📘 Assignment: Working with Python Lists

## 📝 Description

This Python program demonstrates various list operations such as:

- Creating an empty list
- Appending and inserting elements
- Extending a list with another list
- Removing elements
- Sorting in ascending order
- Finding the index of a specific value

The goal of this assignment is to practice **Python list methods** and **manipulation techniques**.

---

## 🚀 Steps Performed

1. **Create an empty list** called `my_list`.
2. **Append** the elements `10`, `20`, `30`, and `40` one by one.
3. **Insert** the value `15` at the second position (index `1`).
4. **Extend** the list with `[50, 60, 70]`.
5. **Remove** the last element from the list.
6. **Sort** the list in ascending order.
7. **Find and print** the index of the value `30`.

---

## 🔍 Step-by-Step Visual Diagram

```
Step 1: Create empty list
[]

Step 2: Append 10
[10]

Append 20
[10, 20]

Append 30
[10, 20, 30]

Append 40
[10, 20, 30, 40]

Step 3: Insert 15 at index 1
[10, 15, 20, 30, 40]

Step 4: Extend with [50, 60, 70]
[10, 15, 20, 30, 40, 50, 60, 70]

Step 5: Remove last element
[10, 15, 20, 30, 40, 50, 60]

Step 6: Sort in ascending order
[10, 15, 20, 30, 40, 50, 60]

Step 7: Find index of 30 → 3
```

---

## 📋 Step Table

```
+-------+--------------------------------------+----------------------------------------+
| Step  | Action                               | List State                             |
+-------+--------------------------------------+----------------------------------------+
| 1     | Create empty list                    | []                                     |
| 2     | Append 10                            | [10]                                   |
|       | Append 20                            | [10, 20]                               |
|       | Append 30                            | [10, 20, 30]                           |
|       | Append 40                            | [10, 20, 30, 40]                       |
| 3     | Insert 15 at index 1                 | [10, 15, 20, 30, 40]                   |
| 4     | Extend with [50, 60, 70]             | [10, 15, 20, 30, 40, 50, 60, 70]       |
| 5     | Remove last element                  | [10, 15, 20, 30, 40, 50, 60]           |
| 6     | Sort in ascending order              | [10, 15, 20, 30, 40, 50, 60]           |
| 7     | Find index of 30                     | Index = 3                              |
+-------+--------------------------------------+----------------------------------------+
```

---

## 💻 Code Example

```python
# ==============================================
# Python List Operations Assignment
# Author: Tasha
# Date: 2025-08-11
# This program demonstrates creating, modifying,
# and querying a Python list in Python.
# ==============================================

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position
my_list.insert(1, 15)

# Step 4: Extend list with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort in ascending order
my_list.sort()

# Step 7: Find and print index of 30
index_of_30 = my_list.index(30)
print("📝 Final List:", my_list)
print("📍 Index of 30:", index_of_30)
```

---

## 📊 Expected Output

```
📝 Final List: [10, 15, 20, 30, 40, 50, 60]
📍 Index of 30: 3
```

---

## 📚 Concepts Learned

- **List creation** (`[]`)
- **append()** to add single elements
- **insert()** to add at a specific position
- **extend()** to combine lists
- **pop()** to remove elements
- **sort()** for ordering
- **index()** to find element positions
