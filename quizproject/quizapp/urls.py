from django.urls import path
from . import views

urlpatterns = [
   
    path('main/',views.main),
    path('register/',views.register,name='register'),
    path('login/',views.loggin, name='login'),
    path('logout/',views.logoutt, name='logout'),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('list_questions/<int:id>/',views.list_question_by_quiz,name="list_question_by_quiz"),
    path('add_options/<int:id>/',views.add_options_by_question,name="add_options_by_question"),
    path('create_topic/',views.create_topic,name="create_topic"),
    path('add_question/<int:id>/',views.add_question, name='add_question')
]
