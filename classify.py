import re

PROBABILITYTABLE = []
DATA_LIST = []
positive = 0.5
negative = 0.5

def constructVocabulary(FILE_NAME):
    """Constructing the vocabulary of the test data"""
    print("compiling test vocabulary")
    f = open(FILE_NAME,'r')
    for line in f:
        line = re.sub('[!@#$.:{}()""-=;,]', '', line)
        for word in line.split():
           if(word not in DATA_LIST):
               DATA_LIST.append(word)

def loadTraining():
    """Loading the probability table from Table file"""
    f = open("Table",r)
    for line in f:
        temparr = []
        temp = line.split()
        temparr.append(temp[0])
        temparr.append(temp[1])
        temparr.append(temp[2])
        PROBABILITYTABLE.append(temparr)

def calculateProbability():
    """Calculating positive and negative probability"""


def classify():
    print("Classification done on assumption - no bias for positive or negative data")
    FILE_NAME = raw_input("\nEnter the file name of the test data:")
    constructVocabulary(FILE_NAME)
    loadTraining()
    calculateProbability()