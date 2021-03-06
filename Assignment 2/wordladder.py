__author__ = 'Timmmmeh'
import string
import Queue

class Find:
    def __init__(self):
        self.dictionary = self.read_dictionary("dictionary")
        self.dictionary = sorted(self.dictionary)
        self.queue = Queue.Queue()
        self.bad_words = []
        self.start_word = self.input()
        self.end_word = self.input()
        # self.start_word = "issue"
        # self.end_word = "weird"
        self.start_change()

    #runs change as many times as it needs to
    def start_change(self):
        word = self.start_word
        parents = [self.start_word]
        self.queue.put({word:parents})
        while self.change(word, parents) == False:
            new_word = self.queue.get()
            word = new_word.items()[0][0]
            parents = new_word.items()[0][1]
        self.restart()


    def change(self, word, parents):
        unchanged = word
        word = list(word)
        new = None
        for letter in range(len(word)):
            for l in string.ascii_lowercase:
                word[letter] = l
                new = ''.join(word)
                # Checks if new is a real word, isn't the same word that was passed in, isnt the same word as the parent
                # and isnt a word that has already been used.
                if self.search(new, self.dictionary) == True and new != unchanged and new != parents[len(parents)-1]\
                        and self.search(new, self.bad_words) == False:
                    # creates a new list
                    lst = list(parents)
                    # adds the new word to the new list
                    lst.append(new)
                    # add the new word and the list to the queue
                    self.queue.put({new:lst})
                    # add the new word to bad words so it wont be found again
                    self.bad_words.append(new)
                    # sort bad words so that it can be searched through
                    self.bad_words.sort()
                # if the new word is the end word then print the path
                if new == self.end_word:
                    print_string = ""
                    # add all the parents to a variable
                    for i in range(len(parents)):
                        print_string += parents[i] + " -> "
                    # print the variable
                    print_string += new
                    print print_string
                    # return True
                    return True
            word = list(unchanged)
        # if there is no q left then there must be no other words that it can match
        # therefore the program must be done
        if self.queue.qsize() == 0:
                print "Connection can not be found"
                return True
        return False

    # Binery search that can take different lists
    def search(self, word, list):
        front_position = 0
        back_position = len(list)-1
        found = False
        #while there are words left and the word hasnt been found
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

    # asks for improt
    def input(self):
        word = raw_input("Enter a 5 letter word ")
        while self.search(word, self.dictionary) == False:
            print "that word is not in the dictionary"
            word = raw_input("Enter a 5 letter word ")
        return word

    # reads all words from the given dictionary
    def read_dictionary(self, location):
        words = []
        with open(location) as item:
            line_number = 0
            for line in item.readlines():
                words.append(line.lower()[:-1])
                line_number += 1
        return words

    #when a link has been shown you can run the programme again
    def restart(self):
        self.bad_words = []
        self.queue = Queue.Queue()
        self.start_word = self.input()
        self.end_word = self.input()
        self.start_change()


if __name__ == '__main__':
    Find()