from django.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
	path('main/', views.login, name='login'),
	path('main/login', views.signIn, name='signIn'),
	path('main/signup', views.signUp, name='signUp'),
	path('main/logout', views.logout, name='logout'),

	path('', views.index, name='index'),
	path('add/', views.addQuestion, name='addQuestion'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
	path('<int:question_id>/vote', views.vote, name='vote'),

]
xurlpatterns = [
	path("", views.index, name='index'),

	# ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/string/x
    path('<str:name>/x/', views.info, name="info"),

]