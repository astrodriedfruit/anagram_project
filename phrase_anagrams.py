import sys

import load_dictionary
from collections import Counter

dictionary = load_dictionary.load('2of4brif.txt')
dictionary.append ('a')
dictionary.append ('i')
dictionary = sorted(dictionary)

user_name = input("Enter a name:")

def find_anagrams(name, word_list):
    nlm = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        wlm = Counter(word.lower())
        for letter in word:
            if wlm[letter] <= nlm[letter]:
                test += letter
        if Counter(test) == wlm:
            anagrams.append(word)
    print(*anagrams, sep="\n")
    print()
    print(f"Remaining letters in {name}")
    print(f"Remaining letters in {len(name)}")
    print(f"Remaining letters in {len(anagrams)}")

def process_choice(name):

    while True:
        choice = input("Make a choice to Enter or start over or # to end")
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice ! ! !")
    name = ''.join(left_over_list)
    return choice, name

def main():
    #Use the name variable and strip out any spaces and/or hyphens
    name = ''.join(user_name.lower().split())
    name = name.replace('-','' )
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace('-','')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase: {len(temp_phrase)}")

            find_anagrams(name, dictionary)
            print("Current anagram phrase =", end=" ")
            print(phrase)

            choice, name = process_choice(name)
            phrase += choice + ''

        elif len(temp_phrase) == limit:
            print("\n***FINISHED!***\n")
            print(phrase)
            print()
            try_again = input('\n\nDo you want to try again? (Press Enter! else "n" to quit)\n')
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()
if __name__ == '__main__':
    main()