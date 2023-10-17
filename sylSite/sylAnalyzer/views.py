from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from sylSite.settings import MEDIA_ROOT
from .forms import UploadFileForm
from .core.doc_creation import init
from .core.section_analysis import *
from .core.score_creation import calculateSylScore
from .core.improvements import createImprovements
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

    #Send the context variable to score_creation.py for score analysis
    #Format as %, update context variable
    sylScore = ("{:.0%}".format(calculateSylScore(context)))
    sylScore = {"syllabusScore": sylScore}
    context.update(sylScore)

    #Send the context variable to improvements.py for improvement analysis
    #Update context variable
    improvements = createImprovements(context)
    context.update(improvements)

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
