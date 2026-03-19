"""
Project to find anagrams! ! !

1. load dictionary into word list X
2. create a list for anagrams X
3. ask the user for a word X
4. loop through word list, compare each 'sorted()' word to your word
5. if the same, add to anagram list
6. print all anagrams with a # of anagrams
"""
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

anagrams = []

user_word = input("Enter word!: ").lower()

for word in word_list:
    if sorted(word) == sorted(user_word) and user_word != word:
        anagrams.append(word)


print(f"Count of anagrams: {len(anagrams)}\n", *anagrams, sep="\n")

# display anagrams
#print(f"Your anagrams: {ana_list}")
    #if word in word_list == word2 in word_list:
    #if the word entered can be rearranged to be one of the words in the word list



