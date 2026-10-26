note = input("Enter your note: ")

# Save the note
with open("notes.txt", "w") as file:
    file.write(note)

# Read the note
with open("notes.txt", "r") as file:
    content = file.read()

print("\nYour saved note:")
print(content)