import os
import glob
from django.core.files.storage import FileSystemStorage

#This function takes user input files, deletes other files in uploads directory, and saves the file to the uploads directory
def saveFile(uploadedFile):

    try:
        #Remove all previous files in the uploads directory
        files = glob.glob('/Users/michaelgagliardi/Documents/GitHub/Syllabus_Project/sylSite/sylAnalyzer/uploads/*')
        for f in files:
            os.remove(f)

        #Save the new file into the uploads directory
        storageFolder = "/Users/michaelgagliardi/Documents/GitHub/Syllabus_Project/sylSite/sylAnalyzer/uploads"
        fs = FileSystemStorage(storageFolder)
        fs.save(uploadedFile.name, uploadedFile)
    except:
        return False
    else:
        return True