import urllib.request
import tkinter as tk
from tkinter import filedialog

#opens file dialog box
def dialogBox():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if ".txt" in file_path:
        #calls both functions
        read_text(file_path)
    else:
        print("The file you have entered is invalid (requires a .txt extension)")

#loads the file and reads it
def read_text(file_path):
    quotes = open(file_path)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

#requests a url and appends the text to it as well as modifying the output
def check_profanity(text_to_check):
    with urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + urllib.parse.quote(text_to_check)) as response:
        output = response.read()
    output = output.decode('ascii')
    if "true" in output:
        print("\n")
        print("Warning:\nThe scanned text contains profanity.")
    if "false" in output:
        print("\n")
        print ("Approved:\nThe scanned text contains no profanity.")
    else:
        print("\n")
        print("Error:\nThe document that was entered was unable to be inspected.")

dialogBox()   

