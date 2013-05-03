#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Opponent(Player):
    """ generated source for Opponent

    """

    def oppLogic(self):
        if (self.hasMulti() == 31):
            if (self.checkStraight() == 15) or (self.checkStraight() == 20):
                return 0
            else:
                self.goForStraight(self.findOne())
                print "ooga booga"
        else:
            if (self.hasMulti() == 0):
                return 0
            else:
                self.goForPairs(self.hasMulti())
        return 0

    def hasMulti(self):
        value = 0
        if (d1.getFaceValue() != d2.getFaceValue()) and (d1.getFaceValue() != d3.getFaceValue()) and (d1.getFaceValue() != d4.getFaceValue()) and (d1.getFaceValue() != d5.getFaceValue()):
            value += 16
        if (d2.getFaceValue() != d1.getFaceValue()) and (d2.getFaceValue() != d3.getFaceValue()) and (d2.getFaceValue() != d4.getFaceValue()) and (d2.getFaceValue() != d5.getFaceValue()):
            value += 8
        if (d3.getFaceValue() != d1.getFaceValue()) and (d3.getFaceValue() != d2.getFaceValue()) and (d3.getFaceValue() != d4.getFaceValue()) and (d3.getFaceValue() != d5.getFaceValue()):
            value += 4
        if (d4.getFaceValue() != d1.getFaceValue()) and (d4.getFaceValue() != d2.getFaceValue()) and (d4.getFaceValue() != d3.getFaceValue()) and (d4.getFaceValue() != d5.getFaceValue()):
            value += 2
        if (d5.getFaceValue() != d1.getFaceValue()) and (d5.getFaceValue() != d2.getFaceValue()) and (d5.getFaceValue() != d3.getFaceValue()) and (d5.getFaceValue() != d4.getFaceValue()):
            value += 1
        return value

    def checkStraight(self):
        return d1.getFaceValue() + d2.getFaceValue() + d3.getFaceValue() + d4.getFaceValue() + d5.getFaceValue()

    def findOne(self):
        if (d1.getFaceValue() == 1):
            return 1
        if (d2.getFaceValue() == 1):
            return 2
        if (d3.getFaceValue() == 1):
            return 3
        if (d4.getFaceValue() == 1):
            return 4
        if (d5.getFaceValue() == 1):
            return 5
        else:
            return 0

    def goForStraight(self, One):
        if (One == 1):
            d1.roll()
        if (One == 2):
            d2.roll()
        if (One == 3):
            d3.roll()
        if (One == 4):
            d4.roll()
        if (One == 5):
            d5.roll()

    def goForPairs(self, value):
        if (value % 2 == 1):
            d5.roll()
        value /= 2
        if (value % 2 == 1):
            d4.roll()
        value /= 2
        if (value % 2 == 1):
            d3.roll()
        value /= 2
        if (value % 2 == 1):
            d2.roll()
        value /= 2
        if (value % 2 == 1):
            d1.roll()


