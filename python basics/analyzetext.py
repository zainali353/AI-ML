with open("notes.txt", "r") as file:
    text = file.read()

# Count words
words = text.split()
total_words = len(words)

# Count characters
total_characters = len(text)

# Count AI, ignoring capitalization
ai_count = text.lower().count("ai")

print("Total words:", total_words)
print("Total characters:", total_characters)
print("Occurrences of AI:", ai_count)