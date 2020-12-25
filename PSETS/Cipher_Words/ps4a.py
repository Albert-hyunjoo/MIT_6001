# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    # 종료 조건: seq가 한 글자인 경우
    if len(sequence) == 1:
        return [sequence]
    else:
        perm_list = []
        for letter in sequence:
            remaining_letters = "".join([e for e in sequence if e != letter])
            subperm_result = get_permutations(remaining_letters)
            for word in subperm_result:
                if letter+word in perm_list:
                    pass
                else:
                    perm_list.append(letter+word)
    return perm_list

if __name__ == '__main__':
#EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    

