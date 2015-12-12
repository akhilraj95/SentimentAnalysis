import re
import math

PROBWORD = []
PROBPOS = []
PROBNEG = []
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
            if(word!="the" and word!="a" and word!="is"):
                if(word not in DATA_LIST):
                    DATA_LIST.append(word)

def loadTraining():
    """Loading the probability table from Table file"""
    f = open("Table",'r')
    for line in f:
        temparr = []
        temp = line.split()
        PROBWORD.append(temp[0])
        PROBPOS.append(temp[1])
        PROBNEG.append(temp[2])

def calculateProbability():
    """Calculating positive and negative probability"""
    p = math.log(positive)
    n = math.log(negative)


    for word in DATA_LIST:
        if(word in PROBWORD):
            index = PROBWORD.index(word)
            p = p + math.log(float(PROBPOS[index]))
            n = n + math.log(float(PROBNEG[index]))
    print("\npositive="+str(p))
    print("\nnegative="+str(n))
    if(p>n):
        print("\nRESULT : POSITIVE")
        print("CONFIDENCE : positive probability "+str(p-n)+" times the negative")
    else:
        print("\nRESULT : NEGATIVE")
        print("CONFIDENCE : negative probability "+str(n-p)+" times the positive")


def classify():
    print("Classification done on assumption - no bias for positive or negative data")
    FILE_NAME = raw_input("\nEnter the file name of the test data:")
    constructVocabulary(FILE_NAME)
    loadTraining()
    calculateProbability()