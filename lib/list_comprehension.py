#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if (num % 2 == 0)]

def make_exclamation(sentence_list):
    return ([f"{sentence}!" for sentence in sentence_list])
        

return_evens([0, 1, 3, 5, 7, 8, 9])
num_list = range(1,10,2)
return_evens(num_list)
return_evens(range(10))

sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
make_exclamation(sentence_list)