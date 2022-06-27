import string

def extract_words(name_of_file):
    # A function returning a list of all the lowecase words in a file
    input_file = open(name_of_file, 'r')
    wordlist = []
    for line in input_file:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    # A function returning true or false checking if a word belongs to a list or not 
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_text():
    # A function returning a string of an encrypted story saved in a file.
    f = open("secretstory.txt", "r")
    story = str(f.read())
    f.close()
    return story