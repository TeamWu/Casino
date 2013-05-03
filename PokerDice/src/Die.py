#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Die(object):
    """ generated source for Die

    """
    faceValue = 0

    def __init__(self):
        self.faceValue = 1

    def roll(self):
        self.faceValue = Math.random() * 6 + 1
        return self.faceValue

    def setFaceValue(self, value):
        self.faceValue = value

    def getFaceValue(self):
        return self.faceValue

    def toString(self):
        result = Integer.toString(self.faceValue)
        return result


