import matplotlib.pyplot as plt

class charPlay:
    
    def __init__(self):
        self.worth=1.0
        self.newWorth=0.0
        self.worthHistory=[]



def tierList(nOfRounds):

    # Creates the chars
    rock = charPlay()
    paper = charPlay()
    scissors = charPlay()
    well = charPlay()
    
    for i in range(0,nOfRounds):

        # Finds worth for this round based on last round win/lose
        rock.newWorth = scissors.worth
        paper.newWorth = well.worth + rock.worth
        scissors.newWorth = paper.worth
        well.newWorth = rock.worth + scissors.worth

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

    # Plots the worth over the course of the rounds
    plt.plot(rock.worthHistory, label='Rock')
    plt.plot(paper.worthHistory, label='Paper')
    plt.plot(scissors.worthHistory, label='Scissors')
    plt.plot(well.worthHistory, label="Well")
    plt.ylabel('Worth')
    plt.xlabel('Round')
    plt.legend()
    plt.show()



    return
