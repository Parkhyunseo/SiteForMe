from __future__ import unicode_literals

from django import forms

from .models import Task
from .utils import Utils

class TaskForm(forms.ModelForm):
	duedate = forms.DateField(widget=forms.DateInput(
				    format=('%d %B, %Y'),
				    attrs={
				        'class':'datepicker',
				        'id':'task_date',
				        'placeholder':'Click',
				    }),
				    input_formats=('%d %B, %Y',),
				    )
	
	class Meta:
		model = Task
		fields = ['content', 'duedate', 'tag']
		widgets = {
		        'content': forms.TextInput(
		            attrs={
		                'class':'validate',
		                'id':'task_text',
		                'placeholder':'Write Youre Task',
		            }),
				'tag': forms.Select(choices=Utils.get_tag_choicelist()),
		}
