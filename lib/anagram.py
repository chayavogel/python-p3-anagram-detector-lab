# your code goes here!

class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # sort self and assign to variable
        # iterate through the list
        # iterate through each word in the list and make it into a list
        # sort it
        # if it's equal to the self, return it
        # otherwise, keep iterating

        sorted_word = sorted(self.word)
        
        i = 0
        response = []

        while i < len(words):
            word_as_list = list(words[i])
            sorted_list_word = sorted(word_as_list)
            if sorted_word == sorted_list_word:
                response.append(words[i])
            i += 1
        print(response)
        return response
                
        

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])