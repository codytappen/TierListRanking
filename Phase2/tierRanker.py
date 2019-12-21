import matplotlib.pyplot as plt

class charPlay:
    
    def __init__(self):
        self.worth=1.0
        self.newWorth=0.0
        self.worthHistory=[]


# Modify to accept a single list containing all history lists

#def tierHistPrint(rockWorthHistory, paperWorthHistory, scissorsWorthHistory, wellWorthHistory):
#
#    # Plots the worth over the course of the rounds
#    plt.plot(rockWorthHistory, label='Rock')
#    plt.plot(paperWorthHistory, label='Paper')
#    plt.plot(scissorsWorthHistory, label='Scissors')
#    plt.plot(wellWorthHistory, label="Well")
#    plt.ylabel('Worth')
#    plt.xlabel('Round')
#    plt.legend()
#    plt.show()
    
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
        listOfChars[:].newWorth = 

    
    return

def tierListPer(nOfRounds):

    # Creates the chars
    rock = charPlay()
    paper = charPlay()
    scissors = charPlay()
    well = charPlay()
    
    for i in range(0,nOfRounds):

        # Finds worth for this round based on last round win/lose
        rock.newWorth = paper.worth*0.25 + scissors.worth*0.75 + well.worth*0.25
        paper.newWorth = (well.worth*0.75 + rock.worth*0.75) + scissors.worth*0.25
        scissors.newWorth = paper.worth*0.75 + rock.worth*0.25 + well.worth*0.25
        well.newWorth = (rock.worth*0.75 + scissors.worth*0.75)+ paper.worth*0.25


        # Normalizes values around one point per player
        tempNorm = rock.newWorth + paper.newWorth + scissors.newWorth + well.newWorth
        
        rock.newWorth = rock.newWorth/tempNorm
        paper.newWorth = paper.newWorth/tempNorm
        scissors.newWorth = scissors.newWorth/tempNorm
        well.newWorth = well.newWorth/tempNorm

        
        
        # Adds the worth for this round to a list to track over time
        rock.worthHistory.append(rock.worth)
        paper.worthHistory.append(paper.worth)
        scissors.worthHistory.append(scissors.worth)
        well.worthHistory.append(well.worth)

        print("\n \n Round " + str(i) + " values: \n")
        print("Rock = " + str(rock.worth))
        print("Paper = " + str(paper.worth))
        print("Scissors = " + str(scissors.worth))
        print("Well = " + str(well.worth))


        # Sets those values for next round
        rock.worth = rock.newWorth
        paper.worth = paper.newWorth
        scissors.worth = scissors.newWorth
        well.worth = well.newWorth

    # End of For loop


    # Calls graph creation function
    tierHistPrint(rock.worthHistory, paper.worthHistory, scissors.worthHistory, well.worthHistory)






    return
