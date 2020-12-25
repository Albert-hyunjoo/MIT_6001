# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import random
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    words = open(str(file_name), "r")
    word_list = words.readline()
    return word_list.split(" ")

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        try:
            self.valid_words = load_words("words_ps4.txt")
        except NameError:
            self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        mapping_dictionary = {}
        count = 0
        # for example, how about "EIaoU"?
        # 기본적으로 VOWEL_LOWER, UPPER를 같이 받고
        # 만약 들어오는 값이 대문자이고, .lower()가 vowel안에?
        for letter in vowels_permutation:
            if letter in VOWELS_UPPER:
                mapping_dictionary[VOWELS_UPPER[count]] = letter
                count += 1
            elif letter in VOWELS_LOWER:
                mapping_dictionary[VOWELS_LOWER[count]] = letter
                count += 1
            if count > len(vowels_permutation):
                break
        return mapping_dictionary

    def apply_transpose(self, transpose_dict):
        new_message = ""
        for i in self.message_text:
            if i in VOWELS_UPPER + VOWELS_LOWER:
                new_message += transpose_dict[i]
            else:
                new_message += i
        return new_message
        
class EncryptedSubMessage(SubMessage):

    def __init__(self, text):
        SubMessage.__init__(self,text)
        self.message_text = text
        try:
            self.valid_words = load_words("words_ps4.txt")
        except NameError:
            self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        maximum_real_words = 0
        decrypted_message = ""
        what_dict = ""
        for permutations in get_permutations("aeiou"):
            num_real_words = 0
            decoded_message = self.apply_transpose(self.build_transpose_dict(permutations))
            for word in decoded_message.split(" "):
                if is_word(self.get_valid_words(),word) == True:
                    num_real_words += 1
                if num_real_words > maximum_real_words:
                    decrypted_message = decoded_message
                    maximum_real_words = num_real_words
                    what_dict = permutations
        return (what_dict, decrypted_message)

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
