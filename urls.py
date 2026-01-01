
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view),
    path("expedition/create/", views.create_expedition),
    path("expedition/update/<int:exp_id>/", views.update_expedition),
    path("reclamation/create/", views.create_reclamation),
    path("reclamation/action/<int:rec_id>/", views.add_reclamation_action),
]
