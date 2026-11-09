
import json

FILE_NAME = "notes.json"


# Load notes from JSON file
def load_notes():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save notes into JSON file
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


# Add a new note
def add_note(notes):
    note = input("Enter your note: ")

    notes.append(note)

    save_notes(notes)

    print("Note saved successfully!")


# View all notes
def view_notes(notes):
    if len(notes) == 0:
        print("No notes available.")
    else:
        print("\nYour Notes:")

        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")


# Count total words
def count_words(notes):
    total = 0

    for note in notes:
        total += len(note.split())

    print("Total words:", total)


# Main program
def main():

    notes = load_notes()

    while True:

        print("\n===== NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Count Words")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            count_words(notes)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
