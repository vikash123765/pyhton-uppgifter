
def replace_words_in_file(filename, old, new):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            modified_text = text.replace(old, new)

        with open(filename, 'w') as file:
            file.write(modified_text)

        print(f'Filen {filename} har uppdaterats.')

    except FileNotFoundError:
        print(f'Filen {filename} hittades inte.')



filename = input('Ange ett filnamn: ')
old = input('Ord att byta ut: ')
new= input('Ersätt med: ')

replace_words_in_file(filename, old, new)

