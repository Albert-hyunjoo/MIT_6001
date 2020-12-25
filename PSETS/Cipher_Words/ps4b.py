import string

def load_words(file_name):
    words = open(str(file_name), "r")
    word_list = words.readline()
    return word_list.split(" ")

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words_ps4.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        try:
            self.valid_words = load_words("words_ps4.txt")
        except NameError:
            self.valid_words = load_words(WORDLIST_FILENAME)
    def __getitem__(self, shift):
        return self.build_shift_dict(shift)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        if shift > 26:
            print("you input wrong shift int.")
            return None
        else:
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            lower_dictionary = {}
            upper_dictionary = {}
            for lower in lowercase:
                modified_location_lower = lowercase.index(lower) + shift
                if modified_location_lower >= len(lowercase):
                    modified_location_lower -= len(lowercase)
                lower_dictionary[lower] = lowercase[modified_location_lower]
            for upper in uppercase:
                modified_location_upper = uppercase.index(upper) + shift
                if modified_location_upper >= len(uppercase):
                    modified_location_upper -= len(uppercase)
                upper_dictionary[upper] = uppercase[modified_location_upper]
            return {**lower_dictionary, **upper_dictionary}

    def apply_shift(self, shift):
        new_message = ''
        for i in self.message_text:
            if i in string.ascii_letters:
                new_message += self.build_shift_dict(shift)[i]
            else:
                new_message += i
        return new_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.get_encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.build_shift_dict(shift).copy()

    def get_message_text_encrypted(self):
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        self.shift = shift
        self.get_encryption_dict = self.build_shift_dict(self.shift)
        self.get_message_text_encrypted = self.build_shift_dict(self.shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        maximum_real_words = 0
        decrypted_word = ""
        best_shift = 0
        for shift in range(26):
            num_real_words = 0
            decoded_word = self.apply_shift(shift)
            for word in decoded_word.split(" "):
                if is_word(self.get_valid_words(), word) == True:
                    num_real_words += 1
            if num_real_words > maximum_real_words:
                decrypted_word = decoded_word
                maximum_real_words = num_real_words
                best_shift = shift
        # self.message_text를 해독하는 것이 목적
        # 어떻게?
        # 0~26까지의 shift value를 모두 순회한다
        # 사전에 maximum value, decrypted_word return
        # 실제 단어와 가장 가까운 경우, apply_shift를 했을 때, 실제 단어와 얼마나 가까운가?
        return (best_shift, decrypted_word)


if __name__ == '__main__':
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
ciphertext1 = CiphertextMessage("Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr o qzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu.")
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
print('Actual Output:', ciphertext1.decrypt_message())

