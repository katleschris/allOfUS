from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#In our poll application, we’ll have the following four views(type of webpage ):

#Question “index” page – displays the latest few questions.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#Question “detail” page – displays a question text, with no results but with a form to vote.
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

#Question “results” page – displays results for a particular question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#Vote action – handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse("You're voting n question %s." % question_id)