from django import forms
from .models import Issue, Comment

class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'body', 'screenshot_url', 'issue_status',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', 'author', 'issue',) 

# I am creating a class in both instances to house our forms. Inside of it we will declare another class. 
# The Meta class within the form contains meta data we have to describe the form. 
# In this case, the model attached to the form and the fields we want to include in our form. 
# Note that the fields are in parenthesis instead of square brackets - they are in a tuple instead of a list! 
# Tuples are like lists but they are immutable -- they can't be changed