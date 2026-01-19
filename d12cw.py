try:
    title = input("Enter book title: ")

    if not title.replace(" ", "").isalpha():
        raise ValueError("Error: Book title must contain only alphabets and spaces.")

    year = input("Enter publication year: ")

    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Publication year must be a 4-digit number starting with 19 or 20.")

    print("\nBook details accepted successfully!")
    print(f"Title: {title}")
    print(f"Publication Year: {year}")

except ValueError as e:
    print(e)

finally:
    print("\nThank you for using the Mini Library System.")
