__author__ = 'Timmmmeh'
import string
import Queue

class Find:
    def __init__(self):
        self.start = None
        self.end = None
        self.dictionary = self.read_dictionary("dictionary")
        self.dictionary = sorted(self.dictionary)
        self.queue = Queue.Queue()
        self.bad_words = []
        """self.start_word = self.input()
        self.end_word = self.input()"""
        self.start_word = "three"
        self.end_word = "honey"
        self.start_change()

    def start_change(self):
        word = self.start_word
        parents = [self.start_word]
        while self.change(word, parents) == False:
            new_word = self.queue.get()
            print new_word
            word = new_word.items()[0][0]
            parents = new_word.items()[0][1]

    def change(self, word, parents):
        unchanged = word
        word = list(word)
        new = None
        for letter in range(len(word)):
            for l in string.ascii_lowercase:
                word[letter] = l
                new = ''.join(word)
                #work on bad_words. not working yet
                if self.search(new, self.dictionary) == True and new != unchanged and new != parents[len(parents)-1] and self.search(new, self.bad_words) == False:
                    lst = parents
                    lst.append(new)
                    self.queue.put({new:lst})
                    self.bad_words.append(new)
                    self.bad_words.sort()
                if new == self.end_word:
                    print new, parents
                    return True
            word = list(unchanged)
        return False

    def search(self, word, list):
        front_position = 0
        back_position  = len(list)-1
        found = False
        while front_position <= back_position and not found:
            midpoint = (front_position + back_position)/2
            if word == list[midpoint]:
                found = True
            else:
                if word < list[midpoint]:
                    back_position = midpoint -1
                else:
                    front_position = midpoint+1
        return found

    def input(self):
        word = raw_input("Enter a 5 letter word ")
        while self.search(word) == False:
            print "that word is not in the dictionary"
            word = raw_input("Enter a 5 letter word ")
        return word


    def read_dictionary(self, location):
        words = []
        with open(location) as item:
            line_number = 0
            for line in item.readlines():
                words.append(line.lower()[:-1])
                line_number += 1
        return words

if __name__ == '__main__':
    Find()