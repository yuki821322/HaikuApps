from django import forms

from .models import Haiku

class HaikuForm(forms.ModelForm):
    class Meta:
      model = Haiku
      fields = ["text","author_name"]
      