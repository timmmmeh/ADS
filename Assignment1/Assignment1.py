import collections

class SpellCheck:
    def __init__(self):
        #simple hash
        dict = {'a':1,'A':1,'b':2,'B':2,'c':3,'C':3,'d':4,'D':4,'e':5,'E':5,
                'f':6,'F':6,'g':7,'G':7,'h':8,'H':8,'i':9,'I':9,'j':10,'J':10,
                'k':11,'K':11,'l':12,'L':12,'m':13,'M':13,'n':14,'N':14,'o':15,'O':15,
                'p':16,'P':16,'q':17,'Q':17,'r':18,'R':18,'s':19,'S':19,'t':20,'T':20,
                'u':21,'U':21,'v':22,'V':22,'w':23,'W':23,'x':24,'X':24,'y':25,'Y':25,
                'z':26,'Z':26}
        #correct words have a hash value, then a list of words that have that value
        correct_words = {}
        self.create_correct_words(correct_words, dict)
        #sort correct words by hash value
        correct_words = collections.OrderedDict(sorted(correct_words.items()))
        #test words have the key which is the word, then a position, then a hash value
        test_words = {}
        self.create_test_words(test_words)
        error_words = {}
        #hash the list of test words
        self.hash(test_words,dict)
        #self.check_test_words(test_words, correct_words, error_words)
        self.search_hash(test_words, correct_words, error_words)
        #create boundaries for the error words
        self.give_bounds(error_words)
        #search for the correct spelling of a word
        self.search_for_correct(error_words, correct_words)

    def create_test_words(self, test_words):
        filename = "error words.txt"
        with open(filename) as item:
            line_number = 0
            for line in item.readlines():
                word_number = 0
                words = line.lower()[:-1]
                for x in words.split(" "):
                    test_words.update({x:[[line_number, word_number]]})
                    word_number += 1
                line_number += 1

    def create_correct_words(self, correct_words, dict):
        temp_dict = {}
        filename = "correct words.txt"
        with open(filename) as item:
            for line in item.readlines():
                words = line.lower()[:-1]
                for x in words.split(" "):
                    temp_dict.update({x:[]})
        self.hash(temp_dict, dict)
        for i in range(len(temp_dict)):
            found = False
            for x in range(len(correct_words)):
                if correct_words.items()[x][0] == temp_dict.items()[i][1][0]:
                    correct_words.items()[x][1].append(temp_dict.items()[i][0])
                    found = True
            if found == False:
                correct_words.update({temp_dict.items()[i][1][0]:[temp_dict.items()[i][0]]})

    def hash(self, test_words, dict):
        for key in test_words:
            running_total = 0
            for letter in key:
                running_total += dict[letter]
            test_words[key].append(running_total)

    def search_hash(self, test_words, correct_words, error_words):
        for i in range(len(test_words)):
            returned_list = self.search(test_words.items()[i][1][1], test_words.items()[i][1][1], test_words.items()[i][0], correct_words)
            if len(returned_list) == 0:
                error_words.update({test_words.items()[i][0]: test_words.items()[i][1]})

    def search_for_correct(self, error_words, correct_words):
        for i in range(len(error_words)):
            returned_list = self.search(error_words.items()[i][1][2], error_words.items()[i][1][3], error_words.items()[i][0], correct_words)
            self.check(returned_list, error_words.items()[i][0], error_words.items()[i][1][0])

    def search(self, lower_bound, upper_bound, word, correct_words):
        list_of_words = []
        while upper_bound >= lower_bound:
            first = 0
            last = len(correct_words)-1
            found = False
            while first <= last and not found:
                midpoint = (first + last)/2
                #if lower bound equals the hash value of a correct word
                if correct_words.items()[midpoint][0] == lower_bound:
                    for i in range(len(correct_words.items()[midpoint][1])):
                        if correct_words.items()[midpoint][1][i] == word:
                            list_of_words.append(correct_words.items()[midpoint])
                            found = True
                        else:
                            found = True
                else:
                    if lower_bound > correct_words.items()[midpoint][0]:
                        first = midpoint + 1
                    elif lower_bound < correct_words.items()[midpoint][0]:
                        last = midpoint - 1
                midpoint = (first + last)/2
                count = 0
                #loop through every hash value between upper bound and lower bound
                for x in range(lower_bound, upper_bound):
                    if correct_words.items()[midpoint][0] == x:
                        list_of_words.extend(correct_words.items()[midpoint][1])
                        if midpoint + 1 < len(correct_words):
                            midpoint += 1
                    elif x > correct_words.items()[midpoint][0]:
                        if midpoint <= len(correct_words)+1:
                            midpoint += 1
                    if len(correct_words) == midpoint:
                        break
                    lower_bound += 1
                    count += 1
            lower_bound += 1
        return list_of_words

    def check(self, list_of_words, check_word, location):
        possible_words = []
        letters = list(check_word)
        for i in range(len(list_of_words)):
            tally = 0
            length = 0
            l = 0
            if len(list_of_words[i]) <= len(letters):
                length = len(list_of_words[i])-1
            else:
                length = len(letters) -1
            while l <= length:
                if l == 0:
                    if letters[l] == list_of_words[i][l] or letters[l] == list_of_words[i][l+1]:
                        tally +=1
                elif l == length:
                    if letters[l] == list_of_words[i][l] or letters[l] == list_of_words[i][l-1]:
                        tally +=1
                else:
                    if letters[l] == list_of_words[i][l] or letters[l] == list_of_words[i][l-1] or letters[l] == list_of_words[i][l+1]:
                        tally +=1
                l += 1
            if tally >= len(list_of_words[i])/2:
                possible_words.append(list_of_words[i])
        print check_word, "at line", location[1], "word number", location[0], "is incorrect, here are some suggestions:", possible_words

    def give_bounds(self, error_words):
        for i in range(len(error_words)):
            if error_words.items()[i][1][1] <= 26:
                error_words.items()[i][1].append(1)
            else:
                error_words.items()[i][1].append((error_words.items()[i][1][1])-26)
            error_words.items()[i][1].append((error_words.items()[i][1][1])+26)

if __name__ == '__main__':
    SpellCheck()

