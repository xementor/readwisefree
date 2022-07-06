from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, User, Vote, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {
            'latest_question_list': latest_question_list,
            'current_user' : current_user,
        }
        return render(request, 'polls/index.html', context)
    else:
        return render(request, 'polls/main.html')
	

	


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.get(pk=request.POST['choice'])
    # choice = get_object_or_404(Choice, pk=request.POST['choice'])
    user = User.objects.filter(username=request.session['user'])[0]

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        vote = Vote(question=question, choice=choice, user=user)
        vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def info(request, name):
	return HttpResponse("Your name is %s" % name) 

def addQuestion(request):

    question_text = (request.POST['question_text'])

    choice1 = request.POST['choice1']
    choice2 = request.POST['choice2']
    choice3 = request.POST['choice3']
    choice4 = request.POST['choice4']

    user = request.session['user']

    if not user:
        user = User.objects.get(pk=1)
    else:
        user = User.objects.filter(name=user)[0]

    
    try:
        question = Question(question_text= question_text, pub_date = timezone.now(), user = user)
        question.save()
        question.choice_set.create(choice_text=choice1, votes=0)
        question.choice_set.create(choice_text=choice2, votes=0)
        question.choice_set.create(choice_text=choice3, votes=0)
        question.choice_set.create(choice_text=choice4, votes=0)
    except Exception as e:
        raise
    else:
        
        return HttpResponse(question.id)

    


def login(request):
    return render(request, 'polls/main.html')

def signIn(request):

    username = request.POST['username']
    password = request.POST['pass']
    try:
        user = User.objects.filter(name=username, password=password)
    except Exception as e:
        raise
    else:
        if user:
            request.session['user'] = username
            return redirect('polls:index')
        else:
            return HttpResponse('username or password is errorjj')

    

def signUp(request):
    username = request.POST['username']
    password = request.POST['pass']
    try:
        user = User(name=username,password=password)
    except Exception as e:
        raise
    else:
        user.save();
        return HttpResponse(user.name + 'crearted succesfully created')

def logout(request):
    del request.session['user']
    return redirect('polls:login') #with message