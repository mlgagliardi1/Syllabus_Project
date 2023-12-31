import os
from django.core.exceptions import ValidationError

def validate_file_extension(file):
    #Define valid extensions (Currently only text/PDF, will implement .doc)
    validExtensions = ['.pdf', '.txt', '.text', '.PDF']
    
    #Split off the extension, compare to validExtensions, raise error if not correct
    ext = os.path.splitext(file.name)[1]
    if not ext.lower() in validExtensions:
        raise ValidationError('Unsupported file extension')
    