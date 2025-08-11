# 📂 File Processor

## 📝 Overview

This Python program reads the content of a text file, converts all the text to **UPPERCASE**, and saves the processed content into another file of your choice. It includes helpful error handling to guide you through common issues like missing files or permission problems.

## 🚀 Features

- 🔍 Reads content from an existing text file (supports `.txt`, `.py`, `.csv`, `.json`, etc.)
- ✨ Converts all text to uppercase for easy text processing practice
- 💾 Saves the processed content to a new or existing output file
- 🛡️ Robust error handling with clear, friendly messages
- 🤝 User-friendly prompts with simple input validation
- 🆕 Option to create a new output file automatically if you don’t have one

## 🛠️ Requirements

- Python 3.x installed on your computer

## 🎯 How to Use

1. Run the program in your Python environment:

   ```bash
   python file_processor.py
   ```

2. When prompted, enter the **name of the input file** (the file you want to process).
3. Decide if you already have an output file to save the results:

   - Type **`y`** to enter the name of your existing output file.
   - Type **`n`** to let the program create a new file called `output.txt`.

4. Sit back and watch the magic happen! 🎩✨ The program will process your file and let you know when it's done.

## 📁 File Location Notes

- Make sure your input file is located in the **same folder** where you run the program, or provide the **full file path**.
- The output file will be created or overwritten in the same location.

## 📚 Example Interaction

```
=== Welcome to my Friendly File Processor ===

This program reads a text file, converts its content to UPPERCASE,
and saves the result to a new file of your choice.

👉 Please enter the name of the file you want to process: input.txt
Do you have an output file to enter processed content? (y/n): n
Great! A new file named 'output.txt' will be created (or overwritten if it exists).

✅ Success! Your file has been processed and saved as 'output.txt'.

Thank you for using my Friendly File Processor! 👋
```

## 🤝 Author

Natasha Hinga
