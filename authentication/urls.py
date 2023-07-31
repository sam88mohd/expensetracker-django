from django.urls import path
from . import views


urlpatterns = [
    path(route='register/', view=views.RegestrationView.as_view(), name='register'),
]
