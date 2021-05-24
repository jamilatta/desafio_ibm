from django.urls import path

from search import views

app_name = "search"
urlpatterns = [
    # Search
    path("", views.search, name="search"),
]
