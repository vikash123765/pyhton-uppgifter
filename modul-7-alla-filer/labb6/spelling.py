
import json


with open('phonetic_alphabet.json', 'r') as alphabet_fil:
    swedish_phonetic_alphabet = json.load(alphabet_fil)

def spell_word_swedish(word, alphabet):
    modified_word = []
    for char in word:
        if char.lower() in alphabet:
            modified_word.append(alphabet[char.lower()])
        else:
            modified_word.append(char)
    return '-'.join(modified_word)


word = input('Word? ')
modified_result = spell_word_swedish(word, swedish_phonetic_alphabet)
print(modified_result)