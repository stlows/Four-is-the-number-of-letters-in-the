from num2words import num2words


def main():
    initial = "Four is the number of letters in the first word of this sentence"
    the_sentence = DevelopTheSentence(201, initial)
    print(the_sentence)
    print("The lengths of the first 201 words are: ")
    for i in range(1, 202):
        if i % 25 == 1:
            print()
            print('{:>3}'.format(i) + ': ', end='')
        print('{:>3}'.format(DetailOnWord(i - 1, the_sentence)[1]) + ' ', end='')
    print()
    print("Length of sentence: " + str(len(the_sentence)))
    print()
    BigSentence(1000, initial)
    #BigSentence(10000, initial)
    #BigSentence(100000, initial)

def DevelopTheSentence(n, initial_string):
    the_string = initial_string
    i = 2
    while len(the_string.split(' ')) < n:
        splitted = the_string.split(' ')
        word = splitted[i - 1].replace(',', '')
        num_letters = len(word.replace('-', ''))
        the_string += ", " + num2words(num_letters) + " in the " + num2words(i, to='ordinal')
        i+=1
    return the_string

def DetailOnWord(n, sentence):
    word = sentence.split(' ')[n].replace(',', '')
    return word, len(word.replace('-', ''))

def BigSentence(n, initial):
    sentence = DevelopTheSentence(n, initial)
    details = DetailOnWord(n - 1, sentence)
    print("The length of word " + str(n) + " [" + details[0] + "] is " + str(details[1]))
    print("Length of sentence: " + str(len(sentence)))

def LengthOfSentence(sentence):
    splitted = sentence.split(' ')
    count = 0
    for word in splitted:
        count+= len(word) + 1
    return count - 1
main()