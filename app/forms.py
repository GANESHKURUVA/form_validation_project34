from django import forms




c=[('python','python'),('django','django'),('sql','sql'),('webtech','webtech'),('java','java'),('mern'
,'mern')]

class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    dateofbirth=forms.DateField()
    education=forms.CharField(max_length=100)
    Mnumber=forms.IntegerField()
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    password=forms.CharField(max_length=8,widget=forms.PasswordInput)