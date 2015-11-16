__author__ = 'Timmmmeh'
class Invert:
    def __init__(self):
        self.dictionary_of_words = {"hello":[], "my":[], "name":[], "is":[], "tim":[], "welp":[]}
        self.read_document()
        self.display()

    def read_document(self):
        line_count = 0
        with open("Document") as item:
            for line in item.readlines():
                word_count = 0
                line_count += 1
                words = line.lower()[:-1]
                for x in words.split(" "):
                    word_count += 1
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
