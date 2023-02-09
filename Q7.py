
import os. path
import sys
def main():
    keywords = {"and", "as", "assert", "break", "class",
    "continue", "def", "del", "elif", "else",
    "except", "False", "finally", "for", "from",
    "global", "if", "import", "in", "is", "lambda",
    "None", "nonlocal", "not", "or", "pass", "raise",
    "return", "True", "try", "while", "with", "yield"}
    filename=input("cities.txt ").strip()
    if not os.path.isfile("filename"): # Check if file exists
       print("File", filename, "does not exist")
       sys.exit()
    infile = open(filename, "r") # Open files for input
    text = infile.read().split() # Read and split words from the file
    count = 0
    for word in text:
       if word in keywords:
          count+= 1
    print("The number of keywords in", filename, "is", count)
main()