
# Full Name: Kevin T Le

# Student ID: 2406054

# Chapman Email: kevle@chapman.edu

# Course Number and Section: CPSC 230-07

# In Class Programming Assignment 5: Exercise #1

# Purpose: This program asks the user to enter a text file.
# All punctuation is removed.
# Every five words in the text will be one line.
# The next five words will create a new line and so on.
# The resulting text file will be written to a seperate text file in the directory called "output.txt"


def read_to_list(txt_file): # This function opens and reads an inputted text file.
                            # It also checks if the file is in the same directory.
    while True:
        try: # opens and reads the text file
            open_txt_file = open(txt_file, 'r')
            read_txt_file = open_txt_file.readlines()
            break
        except: # if text file not in same directory, prompts user to enter another text file.
            txt_file = input("Unable to open file. Please try another file: ")

    return read_txt_file #returns the read text file as a list of words

def write_five(list_of_words, txt_file): # This function takes a list of words, clears punctuation,
                                         # inserts five words per line, and outputs into specified "txt_file"
    clean_list_words = [] # List of strings of words after punctuation removed (spaces stay)
    for string in list_of_words:
        clean_string = "" # Each character that is a letter, number, or space will be put into word string
                          # to be eventually added into a list of strings
        string = string.replace("\n","") # Removes newline character
        for char in string:
            if char.isalnum() == True: # Letters and numbers will be included after filtering
                clean_string += char
            elif char.isspace() == True: # Spaces will be included after filtering
                clean_string += char
            else:
                continue # Skips if not letter, number, or space.
        clean_list_words.append(clean_string) # Resulting word will be appended together with other words as a single string.
                                              # Each resulting strings will be individual elements of list "clean_list_words"

    cleaner_list_words = [] #List after further filtering of clean_list_words

    for element in clean_list_words:
        cleaner_list_words += element.split(" ") #splits string elements into smaller elements of just words for each element

    open_txt_file = open(txt_file, 'w') #opens new text file for writing

    counter = 0
    for word in cleaner_list_words: # Iterates through each word element
                                    # Adds five words to each line before going to new line and repeats
        if counter == 5: # Once there are five words, new line occurs.
            open_txt_file.write("\n")
            counter = 0
        elif counter < 5: # If there are less than 5 words, it adds another word with a space.
                open_txt_file.write(word + " ")
                counter += 1
    # Function does not return anything, only needs to output into seperate file

# Start of Program

file_name = input("Enter your file name: ") #Prompts user to enter file name

write_five(read_to_list(file_name),"output.txt") #Filters inputted text file with above functions and outputs into "output.txt"
