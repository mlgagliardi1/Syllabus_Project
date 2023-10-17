
def createImprovements(context):
    #Create local variables
    improvements = {}
    missingSections = {}
    counter = 0
    #Loop over dictionary values to determine if improvements are needed
    for key in context:
        #Obtain the syllabusScore and its value (stored as str then int)
        if key == "syllabusScore":
            strValue = context[key]
            value = int(strValue.rstrip(strValue[-1]))

            #syllabusScore is between 0 and 25%
            if 0 <= value <= 25:
                #Add improvements message to return dictionary (improvements) using update()
                intermediate = {"improvements": "Major Improvements Recommended:"}
                improvements.update(intermediate)
                #Determine which sections are missing (the value of the key == False if missing)
                for key in context:
                    if context[key] == False:
                        counter += 1
                        #Send the key to updateMissingKeyText() for processing
                        key = updateMissingKeyText(key)
                        #Then add that text to the missingSections dictionary (later appended to improvements and returned)
                        intermediate = {"missingSection" + str(counter): key}
                        missingSections.update(intermediate)
                """
                    Need to add below so context is added to. 
                    Also need to implement template handling
                    of the context variables in results.html.
                """

            #syllabusScore is between 26 and 50%
            elif 26 < value <= 50:
                improvements = "Significant Improvements Recommended: "

            #syllabusScore is between 51 and 75%
            elif 51 < value <= 75:
                improvements = "Minor Improvements Recommended: "

            #syllabusScore is between 76 and 99%
            elif 76 < value <= 99:
                improvements = "Few Improvements Recommended: "
            
            #syllabusScore is 100%
            elif value == 100:
                intermediate = {"improvements": "No Improvements Needed! Great Work. "}
                improvements.update(intermediate)

    #Add the missing sections to improvements and return improvements
    if counter != 0:
        improvements.update(missingSections)
    return improvements
            


#This function formats the output text for missing sections 
def updateMissingKeyText(key):
    if key == "courseInfo":
        key = "Add course Information"
    if key == "instructorInfo":
        key = "Add instructor Information"
    if key == "officeHoursInfo":
        key = "Add Office Hours Information"
    if key == "contactInfo":
        key = "Add Instructor Contact Information"
    if key == "courseDescriptionInfo":
        key = "Add a Course Description"
    if key == "learningOutcomesInfo":
        key = "Add Learning Outcomes"
    if key == "resourcesInfo":
        key = "Add Necessary Resources"
    if key == "gradingScaleInfo":
        key = "Add Grading Scale"
    if key == "participationInfo":
        key = "Add Participation Requirements"
    if key == "midtermInfo":
        key = "Add Midterm Information"
    if key == "finalInfo":
        key = "Add Final Exam Information"
    if key == "courseAdaptationInfo":
        key = "Add Course Adaptation Information"
    if key == "academicEthicsInfo":
        key = "Add Academic Ethics Policies"
    if key == "academicAccomodationsInfo":
        key = "Add Academic Accomodations Information"
    if key == "studentPoliciesInfo":
        key = "Add Student Policies"
    if key == "makeUpPolicyInfo":
        key = "Add Make Up Policy"
    if key == "courseScheduleInfo":
        key = "Add Course Schedule"
    return key