from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question

#In our poll application, we’ll have the following four views(type of webpage ):

#Question “index” page – displays the latest few questions.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = { "latest_question_list": latest_question_list}
    #return HttpResponse(template.render(context, request))
    #The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. 
    #It returns an HttpResponse object of the given template rendered with the given context.
    return render(request, "polls/index.html", context)

#Question “detail” page – displays a question text, with no results but with a form to vote.
#The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

#Question “results” page – displays results for a particular question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#Vote action – handles voting for a particular choice in a particular question.
def vote(request, question_id):
    return HttpResponse("You're voting n question %s." % question_id)