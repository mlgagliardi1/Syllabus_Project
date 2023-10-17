
def createImprovements(context):
    #Create local variables
    improvements = {}
    missingSections = {}
    counter = 0
    #Loop over dictionary values to determine if improvements are needed
    for key in context:
        #Obtain the syllabusScore and its value
        if key == "syllabusScore":
            strValue = context[key]
            value = int(strValue.rstrip(strValue[-1]))

            if 0 <= value <= 25:
                intermediate = {"improvements": "Major Improvements Recommended:"}
                improvements.update(intermediate)

                for key in context:
                    if context[key] == False:
                        counter += 1
                        intermediate = {"missingSection" + str(counter): key}
                        missingSections.update(intermediate)


                """
                    Need to add below so context is added to. 
                    Also need to implement template handling
                    of the context variables in results.html.
                """


            elif 26 < value <= 50:
                improvements = "Significant Improvements Recommended: "

            elif 51 < value <= 75:
                improvements = "Minor Improvements Recommended: "

            elif 76 < value <= 99:
                improvements = "Few Improvements Recommended: "
            
            elif value == 100:
                intermediate = {"improvements": "No Improvements Needed! Great Work. "}
                improvements.update(intermediate)

    #Add the missing sections to improvements and return improvements
    if counter != 0:
        improvements.update(missingSections)
    return improvements
            