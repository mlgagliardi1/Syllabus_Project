import spacy, os, pathlib
from pypdf import PdfReader
from sylSite.settings import MEDIA_ROOT

def init(filename):
    #Declare local variables
    file_extension = ""

    #First, we need to obtain the input file's path (using MEDIA_ROOT) 
    #We must replace " " with "_" to fit Django standards
    noWSFileName = filename.replace(" ", "_")
    INPUT_FILEPATH = os.path.join(MEDIA_ROOT + "\\uploads\\", noWSFileName)

    #Next, we need to determine if it is a txt or PDF using pathlib
    file_extension = pathlib.Path(filename).suffix

    #The file is a PDF
    if file_extension == ".pdf":
        #Convert it to a string
        text = pdfFileToString(INPUT_FILEPATH)
        doc = createDocObject(text)

    #The input file is a text file
    elif file_extension == ".txt" or file_extension == ".text":
        text = textFileToString(INPUT_FILEPATH)
        doc = createDocObject(text)

    #Input file error - should be mitigated by Django framework
    else:
        print("File must be either text or PDF, please retry.")

    #Return the doc object to be manipulated
    return doc



#Function that can read a text file and create a text string for processing
def textFileToString(INPUT_FILEPATH):
    #Declare local variables
    text = ""

    #Open the file in read mode and loop over each line, adding it to text
    file = open(INPUT_FILEPATH, 'r', encoding="UTF-8")
    for line in file:
        text = text + line

    #Close the file once we are done with it
    file.close()

    #Return the text variable
    return text



#Function that can read a PDF file and create a text string for processing
def pdfFileToString(INPUT_FILEPATH):
    #Declare local variables
    text = ""

    #Create a pdfReader instance using pdfReader constructor and filepath
    reader = PdfReader(INPUT_FILEPATH)

    #Loop over each page in the PDF and extract the text
    for page in reader.pages:
        text = text + page.extract_text()

    #Return the text variable
    return text
    


#Function that takes a text string and creates the spacy doc object of it for processing
def createDocObject(text):
    #Load the trained spacy pipeline into a language object (nlp) which will be used to process our string
    nlp = spacy.load("en_core_web_sm")

    #Process the text using our nlp pipeline, creating a document object
    doc = nlp(text)

    #Return the doc object
    return doc