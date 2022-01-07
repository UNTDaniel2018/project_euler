import inflect 

def main(max_num):

    x = inflect.engine()
    letter_sum = 0

    for index in range(1, max_num + 1):
        word = x.number_to_words(index).replace(' ', '').replace('-','')
        letter_sum = letter_sum + len(word)

    return (letter_sum)

if __name__ == '__main__':

    answer = main(1000)
    print(answer)