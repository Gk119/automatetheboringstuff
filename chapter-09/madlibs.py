filename = input("Enter the file name: ")

file = open(filename, 'r')
text = file.read()
file.close()

for word in text.split():
    if word.endswith(('.','!',',',';')):
        word = word[:-1]
    if word == 'ADJECTIVE':
        rep = input("Enter an adjective:\n")
        text = text.replace('ADJECTIVE',rep,1)
    elif word == 'NOUN':
        rep = input("Enter a noun:\n")
        text = text.replace('NOUN',rep,1)
    elif word == 'VERB':
        rep = input("Enter a verb:\n")
        text = text.replace('VERB',rep,1)
    elif word == 'ADVERB':
        rep = input("Enter an adverb:\n")
        text = text.replace('ADVERB',rep,1)

file = open(filename, 'w')
file.write(text)
file.close()