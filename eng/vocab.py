from random import randint
import csv
from pathlib import Path

#todo
#make multiple correct awnsers necceary
#switch up the given language
#add a score system
#make a 3 stryke system
#clean up/correct word to match
#add a "close enouf system"
#show mistake percentage or other indication
#?stryke system?
#put in git repo

#only word list unit 1 is in csv

#add a option to choose what list exist

#'/home/sidneyverite/Desktop/personal stuff/Berufsschuhle/eng/python/vocab.csv'
def readAndMakeList(file,verbose=0):
    vocab = open(file)
    csvreader = csv.reader(vocab)

    header = []
    header = next(csvreader)
    
    vocab_list = []
    
    for row in csvreader:
        vocab_list.append(row)
    if verbose == 1:
        print(vocab_list)
    vocab.close()
    return vocab_list


def frQizz(list):
    used_num = []

    while len(used_num)<len(list):

        r_num=int(randint(0,len(list)-1))

        while r_num in used_num:
            r_num=randint(0,len(list)-1)

        used_num.append(r_num)

        exit = 0
        
        ger_list = list[r_num][1:len(list)-1]
        while exit == 0:
            word_input = str(input("how do you spell {} in german? ".format(str(list[r_num][0]))))

            for word_to_guess in ger_list:
                if word_input == word_to_guess:
                    print("\033[33;1mwow your right\033[0m")
                    exit = 1
            if word_input == "help":
                print(ger_list)

    print("wow you sucke a bit less")    
vocab_list = readAndMakeList(str(Path.cwd()) + '/vocab.csv')
frQizz(vocab_list)
