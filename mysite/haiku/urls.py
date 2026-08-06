from django.urls import path

from.import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.haiku_list, name="haiku_list"),
    path("<int:pk>/", views.haiku_detail, name="haiku_detail"),
]

