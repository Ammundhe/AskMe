from django.urls import path
from . import views
urlpatterns = [
     path('', views.HomePage.as_view(), name="HomePage" ),
    path('ask-question', views.Askquestion.as_view(), name="Askquestion"),
    path('category/<int:category_id>', views.Category.as_view(), name="Category"),
    path('question/<str:slug>', views.Question.as_view(), name="Question"),
    path('question', views.Question.as_view(), name="Question"),
    path('question-answer', views.questionAnswer.as_view(), name="questionAnswer"),
    path('answer/<int:question_id>', views.Answer.as_view(), name="Answer"),    
]
