def mini_library_system():
    try:

        title = input("Enter the book title: ")

        
        if not all(char.isalpha() or char.isspace() for char in title):
            raise ValueError("Error: Book title must contain only alphabets and spaces.")

    
        year = input("Enter the publication year (YYYY): ")

    
        if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
            raise ValueError("Error: Publication year must be a 4-digit number starting with '19' or '20'.")

    
        print(f"Book '{title}' published in {year} has been successfully added to the library.")

    except ValueError as ve:
        print(ve)

    finally:
        print("Program execution completed.")


mini_library_system()