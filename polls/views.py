from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)    

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at results for question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking at votes on question %s." % question_id)
