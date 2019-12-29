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


def buildList():

    # List of Characters
    cList = []

    # Matchup Chart
    WinLose = [[]]

    # Creates all character data types
    for i in range(0, 100):
        print("Enter character name, 0 to stop")
        tempStr = str(input())

        if(tempStr != "0"):
            cList.append(charPlay(tempStr))
        else:
            break
    # End of loop


    # Creates win/loss chart

    print("Please enter the following as a value from 0 to 1")

    for i in range(0, len(cList)):
        tempList = []
        
        for j in range(0, len(cList)):
            print("How does " + cList[i].name + " do against " + cList[j].name)
            tempList.append(float(input()))

        WinLose.append(tempList)

    # End of loop
    

    # Test runs

    tierList(cList, WinLose, 10)

    tierList(cList, WinLose, 20)

    tierList(cList, WinLose, 50)

    tierList(cList, WinLose, 100)

    return


