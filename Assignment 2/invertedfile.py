__author__ = 'jonet5'
import collections

class Invert:
    def __init__(self):
        #list of possible punctuation
        self.puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
        #create the dict of words
        self.dictionary_of_words = {}
        #create list of words that have already been added to the dict
        self.words_used = []
        #reads the Document file
        self.read_document()
        #sorts the dictionary
        self.dictionary_of_words = collections.OrderedDict(sorted(self.dictionary_of_words.items()))
        #prints the dictionary
        self.display()

    def read_document(self):
        #create the line coordinate
        line_count = 0
        with open("Document") as item:
            for line in item.readlines():
                #creates the word coordinate
                word_count = 0
                line_count += 1
                #if at the end remove the /n
                words = line.lower()[:-1]
                for x in words.split(" "):
                    for i in range(len(self.puncList)):
                        #replace all punctuation with nothing
                        x = x.replace(self.puncList[i], "")
                    #convert all uppercase letters to lowercase
                    x = x.lower()
                    word_count += 1
                    #check if the word has already been used
                    if x not in self.words_used:
                        self.words_used.append(x)
                        self.dictionary_of_words.update({x:[[line_count,word_count]]})
                    else:
                        for i in range(len(self.dictionary_of_words)):
                            if x == self.dictionary_of_words.items()[i][0]:
                                self.dictionary_of_words.items()[i][1].append([line_count, word_count])

    def display(self):
        for i in range(len(self.dictionary_of_words)):
            string = self.dictionary_of_words.items()[i][0]
            for x in range(len(self.dictionary_of_words.items()[i][1])):
                string += " " + str(self.dictionary_of_words.items()[i][1][x])
            print string

if __name__ == '__main__':
    Invert()
