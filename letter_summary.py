word = input('Enter a word to get a tally of letters used in the word:' )
result = {}

for letter in word:
    # print("letter: " + letter)
    instance = 0

    for chk_letter in word:
        if chk_letter == letter:
            instance += 1
    
    result[letter] = instance

print(result)
