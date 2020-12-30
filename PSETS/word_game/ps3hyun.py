import random

# loading the word list

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

scrabble_letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, "*" : 0
}

def load_words():
    print("Loading word list from file...")
    words = open("words_ps3.txt", "r")
    word_list = words.readlines()
    word_list_modified = list(map(lambda each:each.strip("\n").lower(), word_list))
    print("play_game not yet implemented")
    return word_list_modified

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    # 점수 얻는 법은 두 개의 component를 곱하는 것
    # 첫번째는 단어 속의 합, 두번째는 (7 * word_length - 3 * (n-word_length) or 1
    # 여기서 word_length는 word의 길이, n은 letters available in the current hand
    word_length = len(word)
    first_score = 0
    second_score = 7 * word_length - 3 * (n-word_length)
    for letter in word:
        first_score += scrabble_letter_values[letter.lower()]
    if second_score > 1:
        return first_score * second_score
    else:
        return first_score * 1

def random_char_vowel(y):
    return ''.join(random.choice(vowels) for x in range(y))

def random_char_consonants(y):
    return ''.join(random.choice(consonants) for x in range(y))

def deal_hand(n):
    vowels_random = get_frequency_dict(random_char_vowel(round(n/3)-1).lower())
    vowels_random["*"]=1
    consonants_random = get_frequency_dict(random_char_consonants(round(n*2/3)).lower())
    return {**vowels_random, **consonants_random}

def display_hand(hand): # hand = dictionary
    hand_visual = ""
    for i in hand.keys():
        if int(hand[i]) == 0:
            hand_visual += ""
        else:
            hand_visual += i * hand[i]
    return (" ".join(hand_visual))

def update_hand(hand, word):
    for i in word:
        try:
            hand[i] -= 1
        except KeyError:
            pass
    return hand

def wild_card_words(word):
    if "*" in word:
        return list(map(lambda x: word.replace("*", x), vowels))
    else:
        return [word]

def is_valid_word(hand, word, word_list): # 현재 핸드, 워드, 워드_리스트
    # 이 단어가 리스트에 존재하는가?
    failure1 = False
    failure2 = False
    for w in wild_card_words(word): # 하나라도 있으면 성립
        if w not in word_list:
            failure1 = False
        else:
            failure1 = True
            break
    for i in word:
        if i not in display_hand(hand):
            failure2 = False
            break
        else:
            failure2 = True
    if (failure1, failure2) == (True, True):
        joint_failure = True
    else:
        joint_failure = False
    return joint_failure

def calculate_handlen(hand):
    return sum(hand.values())

def substitute_hand(hand, letter):
    if letter not in hand.keys():
        print("you selected wrong letter. Try again.")
        return hand
    else:
        hand[letter] -= 1
        word_list_wo_hand_vowels = [e for e in vowels if e not in hand.keys()]
        word_list_wo_hand_consonants = [ e for e in consonants if e not in hand.keys()]
        if letter in vowels:
            hand[random.choice(word_list_wo_hand_vowels)] = 1
        else:
            hand[random.choice(word_list_wo_hand_consonants)] = 1
        if hand[letter] <= 0:
            del hand[letter]
        return hand

def play_hand(hand, word_list):
    score = 0
    hand_copy = hand.copy()
    print("current score: %d" % score)
    print("current hand:" + display_hand(hand_copy))
    while len(display_hand(hand_copy)) != 0:
        typed = input("단어를 입력하세요. '!!' 을 입력하면 게임이 종료됩니다: ")
        if typed == "!!":
            break
        elif is_valid_word(hand_copy, typed, word_list) == False:
            try:
                update_hand(hand_copy, typed)
                print("current hand:" + display_hand(hand_copy))
            except KeyError:
                print("current hand:" + display_hand(hand_copy))
            finally:
                print("다른 단어를 치시오.")
        else:
            print("올바른 단어입니다.")
            score += get_word_score(typed, calculate_handlen(hand_copy))
            print("current score: %d" % score)
            hand_copy = update_hand(hand_copy, typed)
            print("current hand:" + display_hand(hand_copy))
    print("게임이 종료되었습니다. 플레이어의 점수는 %d점입니다." % score)

hand1 = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
calculate_handlen(hand1)
word_list = load_words()
play_hand(hand1, word_list)




    # hand가 나오고
    # 유저는 word를 input한다
    # 어떤 단어가 input되든, is_valid_word의 결과와 상관없이 update가 진행
    # 단어가 invalid하면, 다른 단어를 input하라고 지시한다
    # every word가 valid하면, 1) 남은 글자와 2) 점수가 표시된다
    #
