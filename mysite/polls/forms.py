from django import forms
from django.contrib.auth.models import User
from polls.models import Category, Question, Choice, UserProfile 
from django.forms.widgets import SplitDateTimeWidget

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(max_length=200, help_text = "Please enter the question text")
    pub_date = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'])
                                        
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Question
        exclude = ('category',)



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

  
