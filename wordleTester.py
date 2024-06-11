import time
from main import filter_words, get_most_used_word
from words import word_array as wa, wordle_array as wa_wordle
wordle = False

if wordle:
    waw = wa_wordle
else:
    waw = wa

# returns a response comparing a guessed word to an acutal word
def check_word(guess, actual):
    result = ""
    for i in range(5):
        if guess[i] == actual[i]:
            result += guess[i]
        else:
            if guess[i] not in actual:
                result += "_"
            else:
                pair_else = False
                for letter in enumerate(actual):
                    if letter[0] < i:
                        continue
                    if letter[1] == guess[letter[0]] and letter[1] == guess[i]:
                        result += "_"
                        pair_else = True
                        break
                if not pair_else:
                    result += "/"
    return result

tries = []
under_3 = 0
failes = 0

for i in enumerate(waw):
    print(i[0])
    word_act = i[1][0].lower()
    word_array = wa.copy()
    word = i[1][0]
    complete = False
    invalid_words = []
    attempts = 0
    word = "spald"

    while not complete:
        attempts += 1
        response = check_word(word, word_act)

        blocked_list = []
        eleminate_list = []
        white_list = []
        for letter in enumerate(response):
            if letter[1] == "/":
                white_list.append(word[letter[0]])
                eleminate_list.append([word[letter[0]], letter[0]])
            elif letter[1] == "_":
                if word[letter[0]] not in response and word[
                    letter[0]] not in white_list:
                    blocked_list.append(word[letter[0]])
                else:
                    eleminate_list.append([word[letter[0]], letter[0]])

        filter_words(word_array, response, blocked_list, white_list,
                     eleminate_list, invalid_words)

        if len(word_array) == 1:
            complete = True
        elif word == word_act:
            complete = True
        else:
            if word_array == []:
                print("Error with the word!")
                failes += 1
                complete = True
            else:
                word = get_most_used_word(word_array, invalid_words)[0]
    if attempts <= 3:
        under_3 += 1

    if attempts > 6:
        failes += 1
        print(word_act)
        tries.append(attempts)
    else:
        tries.append(attempts)

avrg = sum(tries) / len(tries)
tot = len(wa)
print(f"Average: {avrg}\n\nPercent Under 3 Tries: {under_3/tot}\n\nFails: {failes}")




