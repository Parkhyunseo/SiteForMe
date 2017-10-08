from __future__ import unicode_literals

from django import forms

from .models import Memo
from .utils import Utils

class MemoForms(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs=
					{
						'class':'materialize-textarea',
						'placeholder':'Write Youre Memo',
				}), label='')
	content_color = forms.CharField(widget=forms.Select(choices=Utils.get_content_color_choicelist())
	, label='')
	
	class Meta:
		model = Memo
		fields = ['content', 'content_color']
