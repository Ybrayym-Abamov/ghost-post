from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.main, name='homepage'),
    path('boasts/', views.boasts),
    path('roasts/', views.roasts),
    path('likes/<int:postid>/', views.upvote),
    path('dislikes/<int:postid>/', views.downvote),
    path('sortscore/<int:post>/', views.sortscore, name='sortscore'),
    path('mostpopular/', views.mostpopular),
    path('ghostsubmission/', views.ghostsubmission),
    # extra credit
    path('posts/<str:private_key>/', views.private_view, name='private'),
    path('delete/<str:pk>/', views.delete_post)
]
