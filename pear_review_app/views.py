from django.shortcuts import render
from .models import Issue, Comment

# Create your views here.

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'pear_review/issue_list.html', {'issues': issues})

def issue_detail(request, pk):
    issue = Issue.objects.get(id=pk)
    return render(request, 'pear_review/issue_detail.html', {'issue': issue})    

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'pear_review/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'pear_review/comment_detail.html', {'comment': comment})

# ^^ On the third line, we see that we are rendering a template. 
# The first argument is the request argument,
# the second is the template that we want to render, 
# and the third is a dictionary with the data we want to send to the view.
# in this case, that's the issue QuerySet with the key 'issues'.



