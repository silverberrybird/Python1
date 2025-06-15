#Take a dictionary element from the user
my_dict = {}
n = int(input("How many items do you want to add to the dictionary? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("Your dictionary:", my_dict)

#Write a Python  program that takes a list of strings and 
# returns a dictionary where the keys are the string lengths, 
# and the values are lists of strings of that length.
l = ["Python", ".Net", "C", "PHP", "Java", "c++"]

d = {}
for word in l:
    length = len(word)
    if length not in d:
        d[length] = []
    d[length].append(word)

print(d)

# Write a program to count the frequency of each word in a given sentence using a dictionary.
str= "Python is great and Python is easy to learn"
d={}
for word in str.split():
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print("Word frequency:", d)


#Write a program to invert a dictionary (swap keys and values).
d={"one": 1, "two": 2, "three": 3}
inverted = {value: key for key, value in d.items()}
print(d)

#Phonebook Application
phonebook = {}

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Count Contacts")
    print("5. Delete Contact")
    print("6. Clear All Contacts")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        if name in phonebook:
            print("Contact already exists. Updating phone number.")
        else:
            print("New contact added.")
        phonebook[name] = phone

    elif choice == "2":
        search = input("Enter name to search: ")
        print("Phone:", phonebook.get(search, "Not found."))

    elif choice == "3":
        print(" All Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

    elif choice == "4":
         print("Total contacts:",len(phonebook))
        
    
    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

    elif choice == "6":
        confirm = input("Are you sure you want to clear all contacts? (yes/no): ").lower()
        if confirm == "yes":
            phonebook.clear()
            print("All contacts cleared.")
        else:
            print("Clear all cancelled.")

    elif choice == "7":
        break
    else:
        print("Invalid choice.")
