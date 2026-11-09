import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
filepath=filedialog.askopenfilename(
     title="Select your note",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)
if filepath:
    with open(filepath, "r", encoding="utf-8") as file:
     text=file.read()
     words=text.split()
     print("Notes contains: ",words)
     count=len(words)
     print("Total words in the notes: ",count)
     search=input("Enter the word to search: ")
    if search in words:
        print("The word ",search," is present in the notes")
    else:
        print("The word ",search," is not present in the notes")
    
