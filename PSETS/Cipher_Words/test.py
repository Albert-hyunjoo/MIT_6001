for letter in "abc":
    remaining_letters = "".join([e for e in "abc" if e != letter])
    print(remaining_letters)
