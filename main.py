import Train
import classify

def train():
    Train.initialise()


choice = raw_input("\nRun training scripts(1/0)-")
if(choice=='1'):
    train()
classify.classify()
