#!/usr/bin/env python3.6

import codecs
from collections import defaultdict
from re import split

def loadCorpus():
    with codecs.open('hi.train.tok', encoding='utf-8') as f:
        words = f.read()
    return split(r'[\s+.,|?]', words)


def getTopTenWords(corpus):
    wordCount = defaultdict(int)
    for word in corpus:
        if word != '':
            wordCount[word] += 1

    sortedWordCount = sorted(wordCount, key = wordCount.get, reverse=True)

    k = 0
    for w in sortedWordCount:
        print(w, wordCount[w])
        k += 1
        if k == 10:
            break


def main():
    corpus = loadCorpus()
    print(f"Total no of words: {len(corpus)}")
    print(f"No of unique words: {len(set(corpus))}")
    print(f"Top 10 words and their frequencies:")
    getTopTenWords(corpus)


if __name__ == '__main__':
    main()
