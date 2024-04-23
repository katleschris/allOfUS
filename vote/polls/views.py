from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice

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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request, 
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1  # instructs the database to increase the vote count by 1.
        selected_choice.save()
        #Always return an HttpResponseRedirected after successfully dealing with Post data. This prevents data from being posted twicr if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))