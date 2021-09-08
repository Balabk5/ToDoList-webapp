from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("form_upload/", views.form_upload, name="form_upload"),
    path("model_form_upload", views.model_form_upload, name="model_form_upload")
]
