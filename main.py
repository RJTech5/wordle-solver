from words import word_array as wa, wordle_array as wa_wordle
invalid_words = []

# Sets wether the script uses all 5 letter words, or just wordles possible soltuions
wordle = True

if wordle:
    wa = wa_wordle

# Returns the letter frequency score of a given word given a frequency code
def get_freq_score(word, code):
    score = 0
    for letter in enumerate(word):
        if letter[0] == 0 or letter[1] not in word[0:letter[0]]:
            score += code[letter[1]]
    return score

# Returns either the word with the largest frequency score, or word with the highest frequency
def get_most_used_word(words, invalid_words):
    letter_frequency = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
                        "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
                        "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
                        "y":0,"z":0,}

    top_word = words[0]
    for word in words:
        invalid = False
        for word_str in invalid_words:
            if word_str == word[0]:
                invalid = True

        if not invalid:
            if word[1] > top_word[1]:
                top_word = [word[0], word[1]]

            for letter in enumerate(word[0]):
                if letter[0] == 0 or letter[1] not in word[0][0:letter[0]]:
                    letter_frequency[letter[1]] += 1

    if wordle:
        top_word = [words[0], get_freq_score(words[0][0], letter_frequency)]
        for word in words:
            invalid = False
            for word_str in invalid_words:
                if word_str == word[0]:
                    invalid = True

            if not invalid:
                score = get_freq_score(word[0], letter_frequency)
                if score > top_word[1]:
                    top_word = [word, score]
        return top_word[0]

    else:
        return top_word

# filters a given wrd array based on parameters
def filter_words(word_array, response, blocked_list, white_list, eleminate_list, invalid_words):
    poped = 0
    for word in enumerate(word_array.copy()):
        # filters word if invalid
        if word[1][0] in invalid_words:
            word_array.pop(word[0] - poped)
            poped += 1
            continue

        short = False
        # filters word if a given letter from eleminate_list is at an associated position in the word
        for letter in eleminate_list:
            if letter[0] == word[1][0][letter[1]]:
                word_array.pop(word[0] - poped)
                poped += 1
                short = True
                break

        if short:
            continue

        # filters word if it has a letter from blocked_list
        for letter in blocked_list:
            if letter in word[1][0]:
                word_array.pop(word[0] - poped)
                poped += 1
                short = True
                break

        if short:
            continue

        # filters word if a letter from response is not in the same place as the word. Builds spots taken list
        spots_taken = []
        for letter in enumerate(response):
            spots_taken = []
            if letter[1] != "_" and letter[1] != "/":
                if letter[1] != word[1][0][letter[0]]:
                    word_array.pop(word[0] - poped)
                    poped += 1
                    short = True
                    break
                else:
                    spots_taken.append(letter[0])

        if short:
            continue

        # filters word if it has one of the misplaced letters on white_list, in the same spot as a spot taken letter
        for misplaced_letter in white_list:
            in_list = False
            for letter in enumerate(word[1][0]):
                if letter[0] not in spots_taken and letter[1] == misplaced_letter:
                    in_list = True
            if not in_list:
                word_array.pop(word[0] - poped)
                poped += 1
                short = True
                break

        if short:
            continue


if __name__ == "__main__":
    word = "spald"
    complete = False
    invalid_words = []

    while not complete:
        print(f"There are {len(wa)} possible words left!\n\n")
        print(
            f"Type '{word}' into wordle\n\nPlease input wordles response below, "
            f"using the correct letters, '_' for absent, and '/' for misplaced\n\nType no if word is invalid...")

        response = input().lower()

        if response == "no":
            invalid_words.append(word)
            word = get_most_used_word(wa, invalid_words)[0]
            continue

        blocked_list = []
        eleminate_list= []
        white_list = []
        for letter in enumerate(response):
            if letter[1] == "/":
                white_list.append(word[letter[0]])
                eleminate_list.append([word[letter[0]], letter[0]])
            elif letter[1] == "_":
                if word[letter[0]] not in response and word[letter[0]] not in white_list:
                    blocked_list.append(word[letter[0]])
                else:
                    eleminate_list.append([word[letter[0]], letter[0]])

        filter_words(wa, response, blocked_list, white_list, eleminate_list, invalid_words)

        if len(wa) == 1:
            print(f"The word is {wa[0][0]}!!")
            complete = True
        else:
            word = get_most_used_word(wa, invalid_words)[0]







