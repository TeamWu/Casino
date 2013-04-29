class Opponent:
    def __init__(self):
        
    def oppLogic(self):
        if hasMulti() == 31:
            if(checkStraight() == 15 || checkStraight() == 20):
                return 0;
            else:
                goForStraight(findOne())
        elif hasMulti() == 0:
            return 0
        else:
            goForPairs(hasMulti())

def hasMulti(self):
        value 
