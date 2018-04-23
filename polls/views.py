from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # qustion = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse("you look at question: %s" % question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
#     # return HttpResponse("you look at results question_id : %s" % question_id)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """查询5条，倒序"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DeleteView):
    template_name = "polls/detail.html"
    model = Question
    # context_object_name = "question1"


class ResultsView(generic.DeleteView):
    template_name = "polls/results.html"
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",
                      {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

        # return HttpResponse("you look at vote page : %s" % question_id)
