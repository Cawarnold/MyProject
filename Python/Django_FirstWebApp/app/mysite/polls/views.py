from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from polls.models import Question

# http://127.0.0.1:8000/polls/
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    template_name = 'polls/index.html'
    #render() : https://docs.djangoproject.com/en/1.7/topics/http/shortcuts/#django.shortcuts.render
    return render(request, template_name, context)


# http://127.0.0.1:8000/polls/1/
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# http://127.0.0.1:8000/polls/1/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# http://127.0.0.1:8000/polls/1/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




#####################################################
################## No Longer Used ###################
#####################################################
'''
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Question

# http://127.0.0.1:8000/polls/
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


# http://127.0.0.1:8000/polls/1/
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

'''