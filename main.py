import movecharacter

def option1():
    # Ask the user to enter their name
    word = input("Enter your word: ")
    # Enter your input
    ch = input("Enter your character: ")
    # Example 1
    output = movecharacter.move_char_to_end(word, ch)
    print("Output move char to end " + output)

def option2():
    # Ask the user to enter their name
    word = input("Enter your word: ")
    # Enter your input
    ch = input("Enter your character: ")
    # Example 2
    output = movecharacter.move_character(word, ch)
    print("Output move character  " + output)

def option3():
    # Ask the user to enter their name
    word = input("Enter your word: ")
    # Enter your input
    ch = input("Enter your character: ")
    # Example 3
    output = movecharacter.remove_character(word, ch)
    print("Remove character " + output)

# Display options to the user
print("Select an option:")
print("1. Move character to end")
print("2. Move character")
print("3. Remove character")

# Ask the user to enter their choice
choice = input("Enter the number of your choice: ")

# Process the user's choice
if choice == "1":
    option1()
elif choice == "2":
    option2()
elif choice == "3":
    option3()
else:
    print("Invalid choice. Please enter a number corresponding to one of the options.")
