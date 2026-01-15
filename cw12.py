try:
    title = input("Enter book title: ")
    
    if not title.replace(" ", "").isalpha():
        raise ValueError("Book title must contain only letters and spaces.")

    year = input("Enter publication year: ")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Publication year must be a 4-digit number starting with 19 or 20.")

    print("\nBook details accepted!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print("\nError:", e)

finally:
    print("\nThank you for using the mini library system.")
