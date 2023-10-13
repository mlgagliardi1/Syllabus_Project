from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from sylSite.settings import MEDIA_ROOT
from .forms import UploadFileForm
from .core.doc_creation import init
from .core.section_analysis import *
import os



# Create your views here.
def homepage(request):
    uploadFileForm = UploadFileForm()
    context = {
        "upload_form": uploadFileForm,
    }
    return render(request, "sylAnalyzer/base_homepage.html", context)



def uploaderror(request):
    uploadFileForm = UploadFileForm()
    context = {
        "upload_form": uploadFileForm,
        "uploaded": False,
    }
    return render(request, "sylAnalyzer/base_homepage.html", context)



def results(request):
    #Create the doc object
    uploadFolder = MEDIA_ROOT + "\\uploads\\"
    for filename in os.listdir(uploadFolder):
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

    #Create the context variable (returned to template render)
    context = {
        "courseInfo": courseInfo,
        "instructorInfo": instructorInfo,
        "officeHoursInfo": officeHoursInfo,
        "contactInfo": contactInfo,
        "courseDescriptionInfo": courseDescriptionInfo,
        "learningOutcomesInfo": learningOutcomesInfo,
        "resourcesInfo": resourcesInfo,
        "gradingScaleInfo": gradingScaleInfo,
        "participationInfo": participationInfo,
        "midtermInfo": midtermInfo,
        "finalInfo": finalInfo,
        "courseAdaptationInfo": courseAdaptationInfo,
        "academicEthicsInfo": academicEthicsInfo,
        "academicAccomodationsInfo": academicAccomodationInfo,
        "studentPoliciesInfo": studentPoliciesInfo,
        "makeUpPolicyInfo": makeUpPolicyInfo,
        "courseScheduleInfo": courseScheduleInfo,
    }
    #Render the results template with the context data
    return render(request, "sylAnalyzer/base_results.html", context)



def examples(request):
    return render(request, "sylAnalyzer/base_examples.html")



def explanation(request):
    return render(request, "sylAnalyzer/base_explanation.html")



def uploaded(request):
    #Create the form using models and forms.py
    form = UploadFileForm(request.POST, request.FILES)

    #Check the request is a POST, contains a file, and the form is valid
    if request.method == "POST" and request.FILES['file'] and form.is_valid():

        #Delete all prior uploads
        uploadFolder = MEDIA_ROOT + "\\uploads\\"
        for filename in os.listdir(uploadFolder):
            file_path = os.path.join(uploadFolder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print ("Failed to delete %s. Reason %s" % (file_path, e))

        #Save the form to the upload directory    
        form.save()
        #Redirect to /results if upload is successful     
        return redirect("/syllabusanalyzer/results")

    else: #form is not valid
        return redirect("/syllabusanalyzer/uploaderror/")
