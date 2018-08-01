from django.shortcuts import render, redirect
from .models import Issue, Comment

from .forms import IssueForm, CommentForm

# Create your views here.

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'pear_review/issue_list.html', {'issues': issues})

def issue_detail(request, pk):
    issue = Issue.objects.get(id=pk)
    return render(request, 'pear_review/issue_detail.html', {'issue': issue})    


def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm()
    return render(request, 'pear_review/issue_form.html', {'form': form})   

def issue_edit(request, pk):
    issue = Issue.objects.get(id=pk)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'pear_review/issue_form.html', {'form': form}) 

def issue_delete(request, pk):
    Issue.objects.get(id=pk).delete()
    return redirect('issue_list')    

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'pear_review/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'pear_review/comment_detail.html', {'comment': comment})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'pear_review/comment_form.html', {'form': form})   

def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment= form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'pear_review/comment_form.html', {'form': form}) 

def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')    


# ^^ On the third line, we see that we are rendering a template. 
# The first argument is the request argument,
# the second is the template that we want to render, 
# and the third is a dictionary with the data we want to send to the view.
# in this case, that's the issue QuerySet with the key 'issues'.



