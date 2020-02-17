# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

from util import Queue
import string

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# Popuplate word_set with all the words from the text file
word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    neighbors = []
    # Split the word into individual characters in a list
    string_word = list(word)

    for i in range(len(string_word)):

        # For every lowercase letter
        # Iterate through every possible combination of changing individual letters in the string
        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter

            # Make the string list back into one string
            w = "".join(temp_word)

            # Check to make sure the word we found is not the original word we sent in
            # Make sure the word exists in the dictionary
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    
print(find_word_ladder("sail", "boat"))