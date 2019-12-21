import matplotlib.pyplot as plt

class charPlay:
    
    def __init__(self):
        self.worth=.25
        self.newWorth=0.0
        self.worthHistory=[]



def tierHistPrint(rockWorthHistory, paperWorthHistory, scissorsWorthHistory, wellWorthHistory):

    # Plots the worth over the course of the rounds
    plt.plot(rockWorthHistory, label='Rock')
    plt.plot(paperWorthHistory, label='Paper')
    plt.plot(scissorsWorthHistory, label='Scissors')
    plt.plot(wellWorthHistory, label="Well")
    plt.ylabel('Worth')
    plt.xlabel('Round')
    plt.legend()
    plt.show()
    
    return



def tierList(nOfRounds):

    # Creates the chars
    rock = charPlay()
    paper = charPlay()
    scissors = charPlay()
    well = charPlay()
    
    for i in range(0,nOfRounds):

        # Finds worth for this round based on last round win/lose
        rock.newWorth = scissors.worth
        paper.newWorth = (well.worth + rock.worth)
        scissors.newWorth = paper.worth
        well.newWorth = (rock.worth + scissors.worth)

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
