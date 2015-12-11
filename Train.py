import re

vocabulary =[]
positve = []
negative = []

def readfile():
    """fucntion to get the data from the training corpus"""
    print(" -reading positive training corpus...")
    f = open("positive.txt",'r')
    for line in f:
        line = re.sub('[!@#$.:{}()""-=;,]', '', line)
        for word in line.split():
           positve.append(word)
           if(word not in vocabulary):
               vocabulary.append(word)
    print(" -reading positive training corpus...")
    f = open("negative.txt",'r')
    for line in f:
        line = re.sub('[!@#$.:{}()""-=;,]', '', line)
        for word in line.split():
            negative.append(word)
            if(word not in vocabulary):
               vocabulary.append(word)


def buildProbabilityTable():
    "creates the probabilty table for each word in the vocabulary"
    f = open('Table','w')
    vocabularysize = len(vocabulary);

    for word in vocabulary:
         positivecount = positve.count(word)
         negativecount = negative.count(word)
         totalcount = positivecount+negativecount
         probpositive = (positivecount+1)/float(totalcount+vocabularysize)
         probnegative = (negativecount+1)/float(totalcount+vocabularysize)
         f.write(word+" "+str(probpositive)+" "+str(probnegative)+"\n")
    f.close()


def initialise():
    print("\ncompiling the vocabulary from training corpus -")
    readfile()
    print("\nbuilding the probability table-")
    buildProbabilityTable()


