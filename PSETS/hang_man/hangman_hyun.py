import random
import string

def list_duplicates_of(word, letter):
    start_at = -1
    locs = []
    while True:
        try:
            loc = word.index(letter,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

# 시작하기 & 메시지 프린팅 (wordslist)

def word_load():
    print("Loading word list from file...")
    words = open("words.txt", "r")
    line = words.readline()
    wordslist = line.split(" ")
    print(("%d words in total loaded!" % len(wordslist)))
    return wordslist

# 별도로 로드해서 프로그램 어디든 접근 가능!

wordslist = word_load()

# 단어의 선택

def word_choice(wordslist):
    return random.choice(wordslist)

random_words = word_choice(wordslist)

def hangman(words, count): # 나중에 random_word를 받을 예정
    word_to_complete = list("_" * len(words))
    words_guessing = list(word_to_complete)
    print("***"+"Target Word:"+"".join(words_guessing)+"***")
    guessed_letters = []
    guessed_words = []
    attempt = int(count)
    # 맞추면 계속 쭉, 틀리면 count 깎이고 종료
    while "_" in words_guessing:
        guess = input("word: ").lower()
        if guess in guessed_letters:
            print("You already guessed this letter. Try again.")
        elif guess.lower() == "hint":
            hint_location = random.choice(list_duplicates_of(words_guessing, "_"))
            words_guessing[hint_location] = words[hint_location]
            guessed_letters.append(words[hint_location])
            print("***"+"Target Word:"+"".join(words_guessing)+"***")
            attempt -= 3
            if attempt <= 0:
                print(("you used all chances. The word is %s. Better next time!" % random_words))
                break
            print(("you have %d attempts" % attempt))
        elif guess == words:
            print(("Congratulations! You got it! The secret word is %s" % words))
        elif guess.lower() != words and len(guess)>2:
            guessed_words.append(guess)
            attempt -= 1
            print("Incorrect! Try again")
            print(("you have %d attempts" % attempt))
        elif len(guess) !=1 or guess.isalpha() == False:
            print("You typed wrong format. Try Again.")
        else:
            if guess in words:
                word_location = list_duplicates_of(words, guess)
                guessed_letters.append(guess)
                for i in word_location:
                    words_guessing[i] = guess
                print("***"+"Target Word:"+"".join(words_guessing)+"***")
                if "_" not in words_guessing:
                    print(("Congratulations! You got it! The secret word is %s" % words))
                    break
            else:
                guessed_letters.append(guess)
                print("no words here! Try again")
                attempt -= 1
                print(("you have %d attempts" % attempt))
                print("***"+"Target Word:"+"".join(words_guessing)+"***")
                if attempt == 0:
                    print(("you used all chances. The word is %s. Better next time!" % random_words))
                    break
    return

hangman(random_words, 15)