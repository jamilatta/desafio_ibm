from django.urls import path

from pet import views

app_name = "pet"
urlpatterns = [
    # Pet
    path(
        "list",
        views.PetList.as_view(),
        name="pet_list",
    ),
    path(
        "create",
        views.PetCreate.as_view(),
        name="pet_create",
    ),
    path(
        "update/<int:pk>",
        views.PetUpdate.as_view(),
        name="pet_update",
    ),
    path(
        "delete/<int:pk>",
        views.PetDelete.as_view(),
        name="pet_delete",
    ),
]
