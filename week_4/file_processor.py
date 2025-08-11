def process_file(input_filename, output_filename):
    """
    Reads a file, processes its content, and writes to a new file with error handling.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path for the output file
    
    Returns:
        bool: True if successful, False if failed
    """
    try:
        # Open and read the entire content from the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Example processing: convert all text to uppercase
        modified_content = content.upper()
        
        # Open the output file and write the modified content
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"\n✅ Success! Your file has been processed and saved as '{output_filename}'.\n")
        return True
    
    except FileNotFoundError:
        print(f"\n❌ Oops! The file '{input_filename}' does not exist. Please check the filename and try again.\n")
    except PermissionError:
        print(f"\n❌ Permission denied when trying to access '{input_filename}'. Check your file permissions.\n")
    except IOError as e:
        print(f"\n❌ An input/output error occurred: {str(e)}\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}\n")
    
    return False


def get_valid_filename(prompt):
    """
    Prompt user for a filename with simple validation.
    
    Args:
        prompt (str): Message to display to user
    
    Returns:
        str: Valid filename entered by user
    """
    while True:
        filename = input(prompt).strip()
        if filename:  # Check that input is not empty
            return filename
        print("⚠️  Please enter a valid filename (it can't be empty).")


def get_output_filename():
    """
    Ask the user if they have an output file to enter processed content.
    If yes, prompt for the filename; if no, return 'output.txt' by default.
    
    Returns:
        str: Output filename
    """
    while True:
        choice = input("Do you have an output file to enter processed content? (y/n): ").strip().lower()
        if choice == 'y':
            filename = input("Please enter the output filename: ").strip()
            if filename:
                return filename
            print("⚠️ Filename cannot be empty. Try again.")
        elif choice == 'n':
            print("Great! A new file named 'output.txt' will be created (or overwritten if it exists).\n")
            return "output.txt"
        else:
            print("❗ Please enter 'y' for yes or 'n' for no.\n")


def main():
    """Main program execution."""
    print("\n=== Welcome to my Friendly File Processor ===\n")
    print("This program reads a text file, converts its content to UPPERCASE,")
    print("and saves the result to a new file of your choice.\n")
    print("👉 Please make sure:")
    print("   • The input file exists and contains text.")
    print("   • The output file will be created or overwritten if it already exists.")
    print("   • Your input file should be located in the same folder where you run this program,")
    print("     or provide the full path to the file.\n")
    print("Examples of input files: .txt, .py, .csv, .json, etc.\n")
    
    # Get input filename from the user
    input_file = get_valid_filename("👉 Please enter the name of the file you want to process: ")
    
    # Get output filename from the user, with choice to create a new file or use an existing one
    output_file = get_output_filename()
    
    # Attempt to process the file and notify the user of the outcome
    process_file(input_file, output_file)
    
    print("Thank you for using my Friendly File Processor! 👋\n")


if __name__ == "__main__":
    main()
