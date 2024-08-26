def introduction_to_python():
    print("Welcome to the Introduction to Python course!")
    print("Let's start with your first Python program.")
    print("The higher the number the harder. ")
    # Exercise: Write a program that prints "Hello, World!"
    print("\nExercise: Write a program that prints 'Hello, World!'\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully printed 'Hello, World!'")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("print('Hello, World!')")
    print("This prints 'Hello, World!' to the console.")

def variables_and_data_types():
    print("\nWelcome to the Variables and Data Types lesson!")
    print("Let's learn about variables and data types in Python.")
    
    # Exercise: Create a variable and assign it an integer value
    print("\nExercise: Create a variable and assign it an integer value.")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully created a variable with an integer value.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("x = 10")
    print("This assigns the integer value 10 to the variable x.")

def control_flow():
    print("\nWelcome to the Control Flow lesson!")
    print("Let's learn about if-else statements and loops in Python.")
    
    # Exercise: Write a program that checks if a number is positive, negative, or zero
    print("\nExercise: Write a program that checks if a number is positive, negative, or zero.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully written a control flow program.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("num = 5")
    print("if num > 0:\n    print('Positive')\nelif num == 0:\n    print('Zero')\nelse:\n    print('Negative')")
    print("This checks if the number is positive, negative, or zero and prints the result.")

def functions():
    print("\nWelcome to the Functions lesson!")
    print("Let's learn how to define and use functions in Python.")
    
    # Exercise: Write a function that takes a number as input and returns its square
    print("\nExercise: Write a function that takes a number as input and returns its square.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully written a function.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("def square(num):\n    return num ** 2")
    print("This defines a function that takes a number and returns its square.")

def lists_and_loops():
    print("\nWelcome to the Lists and Loops lesson!")
    print("Let's learn about lists and loops in Python.")
    
    # Exercise: Write a program that iterates over a list of numbers and prints each number
    print("\nExercise: Write a program that iterates over a list of numbers and prints each number.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully iterated over a list.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("numbers = [1, 2, 3, 4, 5]\nfor num in numbers:\n    print(num)")
    print("This iterates over the list and prints each number.")

def dictionaries():
    print("\nWelcome to the Dictionaries lesson!")
    print("Let's learn about dictionaries in Python.")
    
    # Exercise: Write a program that creates a dictionary and prints its keys and values
    print("\nExercise: Write a program that creates a dictionary and prints its keys and values.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully created and printed a dictionary.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("my_dict = {'a': 1, 'b': 2, 'c': 3}\nfor key, value in my_dict.items():\n    print(key, value)")
    print("This creates a dictionary and prints its keys and values.")

def classes_and_objects():
    print("\nWelcome to the Classes and Objects lesson!")
    print("Let's learn about object-oriented programming in Python.")
    
    # Exercise: Write a class with an attribute and a method, then create an object of that class
    print("\nExercise: Write a class with an attribute and a method, then create an object of that class.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully created a class and an object.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("class MyClass:\n    def __init__(self, value):\n        self.value = value\n    def display(self):\n        print(self.value)\n\nobj = MyClass(10)\nobj.display()")
    print("This defines a class with an attribute and a method, and creates an object of that class.")

def file_handling():
    print("\nWelcome to the File Handling lesson!")
    print("Let's learn how to read from and write to files in Python.")
    
    # Exercise: Write a program that writes to a file and reads from it
    print("\nExercise: Write a program that writes to a file and reads from it.\n")
    
    while True:
        # Test the user's code
        user_code = input("Type your code here and press Enter to test: ")
        try:
            exec(user_code)
            print("Congratulations! You've successfully handled file operations.")
            break
        except Exception as e:
            print("Error executing your code:", e)
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != 'yes':
                break
    
    # Solution
    print("\nSolution:")
    print("with open('example.txt', 'w') as f:\n    f.write('Hello, file!')\n\nwith open('example.txt', 'r') as f:\n    print(f.read())")
    print("This writes 'Hello, file!' to a file and reads it back.")

def main():
    while True:
        print("\nWelcome to the Interactive Python Learning Course!")
        print("Select a lesson to begin:")
        print("1. Introduction to Python")
        print("2. Variables and Data Types")
        print("3. Control Flow")
        print("4. Functions")
        print("5. Lists and Loops")
        print("6. Dictionaries")
        print("7. Classes and Objects")
        print("8. File Handling")
        # Print other lesson options...
        
        choice = input("Enter the number of the lesson you want to start (or 'exit' to quit): ")
        
        if choice == '1':
            introduction_to_python()
        elif choice == '2':
            variables_and_data_types()
        elif choice == '3':
            control_flow()
        elif choice == '4':
            functions()
        elif choice == '5':
            lists_and_loops()
        elif choice == '6':
            dictionaries()
        elif choice == '7':
            classes_and_objects()
        elif choice == '8':
            file_handling()
        elif choice.lower() == 'exit':
            print("Thank you for using the Interactive Python Learning Course. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
