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
def tierList(listOfChars, 2dWinLoss, nOfRounds):

    
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
                listOfChars[j].newWorth+=listOfChars[k].worth*2dWinLoss[j][k]
            
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

    # Simple Rock paper scissors test case
    RPSW = [charPlay(Rock),charPlay(Paper),charPlay(Scissors),charPlay(Well)]

    2dWinLose = [[0,0.25,0.75,0.25],[0.75,0,0.25,0.75],[0.25,0.75,0,0.25],[0.75,0.25,0.75,0]
    
    tierList(RPSW,2dWinLose,20)


