"""
    This document uses the spacy matcher to compare strings 
    (i.e. "course information") to created patterns (pattern = {}).
    If the pattern is found, the function returns true, if it is not
    found, the function returns false.

    Patterns can be added to increase effectiveness of these matching
    functions.
"""



from spacy.matcher import Matcher

def containsCourseInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    courseInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "course"}, {"LOWER": "information"}]
    #Add the pattern to the matcher
    matcher.add("CourseInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        courseInfo = True

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
        
    #Return the courseInfo boolean
    return courseInfo
   


def containsInstructorInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    instructorInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "instructor"}, {"LOWER": "information"}]
    #Add the pattern to the matcher
    matcher.add("InstructorInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        instructorInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return instructorInfo    
    
    
    
def containsOfficeHoursInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    officeHoursInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "office"}, {"LOWER": "hours"}]
    #Add the pattern to the matcher
    matcher.add("OfficeHoursInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        officeHoursInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return officeHoursInfo     
    
    

def containsContactInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    contactInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "contact"}, {"LOWER": "information"}]
    #Add the pattern to the matcher
    matcher.add("ContactInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        contactInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return contactInfo



def containsCourseDescriptionInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    courseDescriptionInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "course"}, {"LOWER": "description"}]
    #Add the pattern to the matcher
    matcher.add("CourseDescriptionInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        courseDescriptionInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return courseDescriptionInfo     
        


def containsLearningOutcomesInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    learningOutcomesInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "learning"}, {"LOWER": "outcomes"}]
    #Add the pattern to the matcher
    matcher.add("LearningOutcomesInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        learningOutcomesInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return learningOutcomesInfo 



def containsResourcesInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    resourcesInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "resources"}]
    #Add the pattern to the matcher
    matcher.add("ResourcesInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        resourcesInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return resourcesInfo  



def containsGradingScaleInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    gradingScaleInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "grading"}, {"LOWER": "scale"}]
    #Add the pattern to the matcher
    matcher.add("GradingScaleInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        gradingScaleInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return gradingScaleInfo  



def containsParticipationInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    participationInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "participation"}]
    #Add the pattern to the matcher
    matcher.add("ParticipationInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        participationInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return participationInfo  



def containsMidtermInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    midtermInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "midterm"}, {"LOWER": "exam"}]
    #Add the pattern to the matcher
    matcher.add("MidtermInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        midtermInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return midtermInfo  



def containsFinalInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    finalInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "final"}, {"LOWER": "exam"}]
    #Add the pattern to the matcher
    matcher.add("FinalInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        finalInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return finalInfo  



def containsCourseAdaptationInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    courseAdaptationInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "course"}, {"LOWER": "adaptation"}]
    #Add the pattern to the matcher
    matcher.add("CourseAdaptationInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        courseAdaptationInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return courseAdaptationInfo  



def containsAcademicEthicsInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    academicEthicsInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "academic"}, {"LOWER": "ethics"}]
    #Add the pattern to the matcher
    matcher.add("AcademicEthicsInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        academicEthicsInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return academicEthicsInfo  



def containsAcademicAccomodationInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    academicAccomodationInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "academic"}, {"LOWER": "accomodation"}]
    #Add the pattern to the matcher
    matcher.add("AcademicAccomodationInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        academicAccomodationInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return academicAccomodationInfo  



def containsStudentPoliciesInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    studentPoliciesInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "student"}, {"LOWER": "policies"}]
    #Add the pattern to the matcher
    matcher.add("StudentPoliciesInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        studentPoliciesInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return studentPoliciesInfo  



def containsMakeUpPolicyInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    makeUpPolicyInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "make"}, {"LOWER": "up"}, {"LOWER": "policy"}]
    #Add the pattern to the matcher
    matcher.add("MakeUpInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        makeUpPolicyInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return makeUpPolicyInfo 



def containsCourseScheduleInformation(doc):
    #Initialize a local boolean (contains course information) - returned
    courseScheduleInfo = False
    #initalize spacy matcher
    matcher = Matcher(doc.vocab)
    #Define the pattern we are looking for
    pattern = [{"LOWER": "course"}, {"LOWER": "schedule"}]
    #Add the pattern to the matcher
    matcher.add("CourseScheduleInformation", [pattern])
    #Apply the matcher to the doc
    matches = matcher(doc)
    #Check if there are any matches, and if so update the courseInfo bool
    if matches:
        courseScheduleInfo = True  

        """     TEMPORARILY PRINT THE MATCHED VALUES AND THEIR LOCATION     """

        for match_id, start, end in matches:
            string_id = doc.vocab.strings[match_id]     #Get string representation
            span = doc[start:end]                       #The matched span
            print(string_id, start, end, span.text)
             
    #Return the courseInfo boolean
    return courseScheduleInfo  