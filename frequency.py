""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import collections

book = '/home/aurora/ToolBox-WordFrequency/iliad.txt'


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == 1:
        curr_line += 1
    lines = lines[curr_line+1:]

    exclude = set(string.punctuation)
    lines = ''.join(a for a in lines if a not in exclude)
    words = lines.split()
    wordlist = []
    for word in words:
        wordlist.append(word)
    wordlist = [word.lower() for word in wordlist]
    wordlist = [word.strip(string.punctuation) for word in wordlist]
    return wordlist


get_word_list(book)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.
    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    dic = dict()
    dic = collections.Counter(word_list)
    topwords= []
    topwords = sorted(dic, key=dic.get, reverse= True)
    return topwords[:n]



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
wordlist = get_word_list(book)
topwords = get_top_n_words(wordlist, 100)
print('Top', len(topwords), 'Words:')
print(topwords)
