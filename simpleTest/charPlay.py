class charPlay:
    
    def __init__(self):
        self.worth=1.0
        self.newWorth=0.0



def tierList(nOfRounds):

    # Creates the chars
    rock = charPlay()
    paper = charPlay()
    scissors = charPlay()
    well = charPlay()
    
    for i in range(0,nOfRounds):

        # Finds worth for this round based on last round win/lose
        rock.newWorth = scissors.worth
        paper.newWroth = well.worth + rock.worth
        scissors.newWorth = paper.worth
        well.newWorth = rock.worth + scissors.worth

        # Sets those values for next round
        rock.worth = rock.newWorth
        paper.worth = paper.newWorth
        scissors.worth = scissors.newWorth
        well.worth = well.newWorth

        print("\n \n Round " + str(i) + "values: \n")
        print("Rock = " + str(rock.worth))
        print("Paper = " + str(paper.worth))
        print("Scissors = " + str(well.worth))


    return
