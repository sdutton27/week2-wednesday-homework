# Simon Dutton
# Due March 23, 2023
# Week 2, Day 3 Homework
#
# Calculations Module to be used with Question #2 for the Homework

from math import pi

def getSqFootage(length, width):
    """
    getSqFootage(length:float, width:float)
    This function expects 2 inputs: the length and width of a house. It
    calculates and returns the square footage of a house with those dimensions.
    """
    area = length * width
    return area

def getCircumference(radius):
    """
    getCircumference(radius:float)
    This function expects an input of the radius of a circle. It calculates and 
    returns the circumference of a circle with the given radius.
    """
    circum = 2 * pi * radius
    return circum