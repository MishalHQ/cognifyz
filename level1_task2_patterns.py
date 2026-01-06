def print_pyramid(rows):
    """Print a number pyramid pattern"""
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print ascending numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def print_reverse_pyramid(rows):
    """Print a reverse number pyramid"""
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def print_diamond(rows):
    """Print a diamond number pattern"""
    # Upper half
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    # Lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def print_floyd_triangle(rows):
    """Print Floyd's triangle"""
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

def print_pascal_triangle(rows):
    """Print Pascal's triangle"""
    for i in range(rows):
        # Print spaces
        print(" " * (rows - i), end="")
        
        # Calculate and print values
        num = 1
        for j in range(i + 1):
            print(num, end="   ")
            num = num * (i - j) // (j + 1)
        print()

def number_pattern_generator():
    """Main function to generate various number patterns"""
    print("=" * 50)
    print("Number Pattern Generator")
    print("=" * 50)
    
    while True:
        print("\nSelect a pattern:")
        print("1. Number Pyramid")
        print("2. Reverse Pyramid")
        print("3. Diamond Pattern")
        print("4. Floyd's Triangle")
        print("5. Pascal's Triangle")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '6':
            print("Thank you for using the pattern generator! 👋")
            break
        
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice! Please try again.")
            continue
        
        try:
            rows = int(input("Enter number of rows: "))
            if rows <= 0:
                print("Please enter a positive number!")
                continue
            
            print()
            if choice == '1':
                print_pyramid(rows)
            elif choice == '2':
                print_reverse_pyramid(rows)
            elif choice == '3':
                print_diamond(rows)
            elif choice == '4':
                print_floyd_triangle(rows)
            elif choice == '5':
                print_pascal_triangle(rows)
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    number_pattern_generator()
