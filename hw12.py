try:
    name = input("Enter your name: ").strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    feedback = input("Enter your feedback: ").strip()
    
    if not feedback:
        raise ValueError("Feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print("\nError:", e)

finally:
    print("\nThank you for visiting our restaurant!")
