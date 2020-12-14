from django import forms

#ToDoのフォーム
class CreateForm(forms.Form):
    do = forms.CharField(label='add ', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
