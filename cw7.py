items = ["milk", "bread", "eggs"]

def add_item(items):
    items.append("butter")
    print(items)
add_item(items)

def remove_last_item(items):
    items.pop()
    print(items) 
remove_last_item(items)

print_item = lambda item: print("Item:", item)
for item in items:
    print_item(item)
    
def count_characters(items):
    if items == []:
        return 0
    return len(items[0]) + count_characters(items[1:])
print("Total characters:", count_characters(items))
