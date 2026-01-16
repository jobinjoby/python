item = input("Enter item name: ")

file = open("items.txt", "a")   
file.write(item + "\n")
file.close()

print("\nItems in the shop:")

file = open("items.txt", "r")
print(file.read())

file.close()

print("Done")
