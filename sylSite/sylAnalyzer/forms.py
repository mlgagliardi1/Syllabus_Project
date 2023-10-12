from django import forms
from .validators import validate_file_extension
from .models import UploadFileModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = "__all__"