### ✅ Week 1
- [calculator](calculator.py) – A Python program that acts as a basic calculator and supports several arithmetic operations. (See details below 👇)

---

## 📁 calculator

A simple Python calculator script that supports various arithmetic operations between two numbers. This script is designed as part of the PLP Python assignments and demonstrates fundamental programming concepts like input/output, conditionals, functions, and error handling.

### ✨ Features
- Supports **addition (+)**, **subtraction (-)**, **multiplication (*)**, **division (/)**  
- Also includes **modulus (%)**, **exponentiation (**)**, and **floor division (//)**
- Handles invalid operations and division/modulus by zero
- Gracefully handles invalid (non-numeric) input
- Displays expressions in a readable format
- Provides friendly user messages, including emojis 😊 and a thank-you message 🎉
- Ends with a goodbye emoji 👋
- Contains **clear inline comments** to help readers understand what’s happening at each step

### 🚀 Usage
To run the calculator, navigate to the folder in your terminal and run:

```bash
python calculator.py

```
### 🛠️ Example output:
```
🔢 Welcome to my basic Python Calculator!
Available operators: +  -  *  /  %  **  //
Enter the first number: 4
Enter an operator: //
Enter the second number: 0

🧮 Expression: 4.0 // 0.0
✅ Result: ❌ Error: Floor division by zero is not allowed.

Would you like to perform another calculation? (yes/no): yes
Enter the first number: 2
Enter an operator: +
Enter the second number: 2

🧮 Expression: 2.0 + 2.0
✅ Result: 2.0 + 2.0 = 4.0

Would you like to perform another calculation? (yes/no): no

🙏 Thank you for using the calculator. Byeeeee! 😊
