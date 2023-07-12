from django import forms
def validate1(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('name should not start with a')
def validate2(name):
    if len(name)<=5:
        raise forms.ValidationError('length must be 5')


class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate1,validate2])
    sage=forms.IntegerField()
    #email=forms.EmailField(validators=[validate1])
    email=forms.EmailField()
    re_email=forms.EmailField()
    url=forms.URLField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_email']
        if e!=re:
            raise forms.ValidationError('not matched')
    def clean_botcatcher(self):#clean_element method only for catching bots 
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')

    

