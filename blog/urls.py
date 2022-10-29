from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleFormView,
    ArticleUpdateView,
    ArticleDeleteView,
)
app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view() , name="index"),
    path("<int:pk>" , ArticleDetailView.as_view() , name="detailView"),
    path("create/" , ArticleFormView.as_view() , name="Create"),
    path("<int:pk>/update/" , ArticleUpdateView.as_view() , name="update"),
    path("<int:pk>/delete/",ArticleDeleteView.as_view() , name="delete")

]
