from django.urls import path
from comments import views

urlpatterns = [
    path('', views.CommentView.as_view()),
    path('<int:id>', views.CommentSingleView.as_view()),
]