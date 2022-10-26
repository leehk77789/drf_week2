from django.urls import path
from articles import views

urlpatterns = [
    path("", views.articleAPI, name="articleAPI"),
    path("<int:article_id>", views.articleDetailApi, name="articleDetailApi"),
]