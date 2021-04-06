################################################################################
# Author: Michael Curry
# Date: 04/05/2021
# Description Program takes user input and translates it, given the pig latin
# representation of the given code.
################################################################################
    
def main():

    text = str(input('Enter a string: ')) # User input
    new_text = pig(text) # Transfering to function
    print(new_text)

    return

def pig(s_tring):

    word_split = s_tring.split() # Splitting the text
    translated = [] # Empty list to append to

    for _ in word_split:
        translation = _[1:] + _[0] + 'ay' # Take the remaing words, adding the first letter to the end and then finally adding 'ay' to it
        translated.append(translation)

    joined = ' '.join(translated) # Conjoing all the translated words
    
    return joined.capitalize() # Can't forget to capitalize
    
if __name__ == '__main__':
    main()
