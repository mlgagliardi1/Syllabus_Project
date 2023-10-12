"""
This will be our hub. From here we will create the doc object,
send it to be manipulated, and return it to the views as needed.
"""

from .doc_creation import init
from .section_analysis import *

def _init_(filename):
    doc = init(filename)

    #Run the section analysis functions from section_analysis.py
    courseInfo = containsCourseInformation(doc)
    instructorInfo = containsInstructorInformation(doc)
    officeHoursInfo = containsOfficeHoursInformation(doc)
    contactInfo = containsContactInformation(doc)
    courseDescriptionInfo = containsCourseDescriptionInformation(doc)
    learningOutcomesInfo = containsLearningOutcomesInformation(doc)
    resourcesInfo = containsResourcesInformation(doc)
    gradingScaleInfo = containsGradingScaleInformation(doc)
    participationInfo = containsParticipationInformation(doc)
    midtermInfo = containsMidtermInformation(doc)
    finalInfo = containsFinalInformation(doc)
    courseAdaptationInfo = containsCourseAdaptationInformation(doc)
    academicEthicsInfo = containsAcademicEthicsInformation(doc)
    academicAccomodationInfo = containsAcademicAccomodationInformation(doc)
    studentPoliciesInfo = containsStudentPoliciesInformation(doc)
    makeUpPolicyInfo = containsMakeUpPolicyInformation(doc)
    courseScheduleInfo = containsCourseScheduleInformation(doc)


    #For now, print the results of the above analysis to terminal
    print("Course Info Present: " + str(courseInfo))
    print("Instructor Info Present: " + str(instructorInfo))
    print("Office Hours Present: " + str(officeHoursInfo))
    print("Contact Info Present: " + str(contactInfo))
    print("Course Description Present: " + str(courseDescriptionInfo))
    print("Learning Outcomes Present: " + str(learningOutcomesInfo))
    print("Resources Present: " + str(resourcesInfo))
    print("Grading Scale Present: " + str(gradingScaleInfo))
    print("Participation Present: " + str(participationInfo))
    print("Midterm Info Present: " + str(midtermInfo))
    print("Final Info Present: " + str(finalInfo))
    print("Course Adaptation Present: " + str(courseAdaptationInfo))
    print("Academic Ethics Present: " + str(academicEthicsInfo))
    print("Academic Accomodations Present: " + str(academicAccomodationInfo))
    print("Student Policies Present: " + str(studentPoliciesInfo))
    print("Make Up Policy Present: " + str(makeUpPolicyInfo))
    print("Course Schedule Present: " + str(courseScheduleInfo))