from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_users, name="get_all_users"),
    path("user/<str:davidson>", views.get_by_davidson),
    path("data/", views.user_manager),
]
