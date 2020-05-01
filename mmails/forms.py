from django import forms


class EmailForm(forms.Form):
    to = forms.EmailField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'tbox'}))
    subject = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class' : 'tbox'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows' : '20','placeholder' : 'Enter Text','class' : 'msg'}),max_length=1000,required=False)
