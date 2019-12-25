import matplotlib.pyplot as plt

class charPlay:
    
    def __init__(self, name):
        self.name = name
        self.worth=1.0
        self.newWorth=0.0
        self.worthHistory=[]


# Accepts a list of worth history lists to graph and a list of characters to label the graphs
def tierHistPrint(listOfChars):
    
    # Plots the worth over the course of the rounds
    for i in range(0, len(listOfChars)):
        plt.plot(listOfChars[i].worthHistory, label=listOfChars[i].name)
    plt.ylabel('Worth')
    plt.xlabel('Round')
    plt.legend()
    plt.show()
    
    return


# Creates the tierlist
def tierList(listOfChars, TwoDWinLoss, nOfRounds):

    
    # Full algorithm
    for i in range(0,nOfRounds):
        
        # Value used to keep values normalized
        normBase=0.0

        # Finds new worth value for each char based on previous round
        # and matchup table
        for j in range(0, len(listOfChars)):

            listOfChars[j].newWorth=0
            
            # Adds the value for each character matchup
            for k in range(0, len(listOfChars)):
                listOfChars[j].newWorth+=listOfChars[k].worth*TwoDWinLoss[j][k]
            
            normBase+=listOfChars[j].newWorth
            
        # Normalizes values
        for j in range(0, len(listOfChars)):
            listOfChars[j].newWorth = listOfChars[j].newWorth/normBase
            listOfChars[j].worth = listOfChars[j].newWorth
            listOfChars[j].worthHistory.append(listOfChars[j].worth)

        # End of main loop


    # Prints the whole history
    tierHistPrint(listOfChars)
    
    return


def main():

    # Building middle complexity melee input data
    meleeChars = []



    # Creates all chars

    meleeNames = ["Fox","Falco","Marth","Sheik","Jigglypuff","Peach","Falcon","Pikachu","Samus","MdMario","Yoshi","Luigi","Ganon","Mario","YoungLink","Donkey","link","GameAndWatch","Roy","Mewtwo","Zelda","Ness","Pichu","Bowser","Kirby"]
    
    for j in range(0,16):
        meleeChars.append(meleeNames[j])

    fox =    [.5,.5,.5,.6,.6,.6,.6,.7,.7,.5,.8,.7,.7,.6,.7,.7,.8,.8,.7,.8,.8,.8,.8,.8,.8]
    falco =  [.5,.5,.5,.5,.5,.5,.5,.7,.7,.5,.6,.8,.7,.6,.6,
            

    
    tierList(RPSW,WinLose,20)

    return


# Allows for simple data entry
def buildCharData(numOfChars):
    
    charList=[]

    WinLose=[][]
    
    for i in range(0,numOfChars):
        print("Character name?")
        for j in range(0, numOfChars):
            

    return




