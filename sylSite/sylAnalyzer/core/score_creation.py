from .section_analysis import *

def calculateSylScore(context):
    #Create local variables
    totalSylSections = 17
    counter = 0
    sylScore = 0
    #Loop over dictionary values to determine how many sections are present
    for value in context.values():
        if value == True:
            counter += 1
    #Calculate and return the syllabus score
    sylScore = counter/totalSylSections
    return sylScore
   