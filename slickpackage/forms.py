from django import forms
from .models import Snippet
from .models import Snippetquote


class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(label='Email')
	body = forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):
	class Meta:
		model = Snippet
		fields = ('name', 'subject', 'body')
		widgets = {
            'name': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'subject': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
             'body': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
             }
	
class Snippetquote(forms.ModelForm):
	class Meta:
		model = Snippetquote
		fields = ('Name', 'Email', 'ContactNumber', 'PackageType', 'Dimensions','Quantity' , 'Specification')
		      