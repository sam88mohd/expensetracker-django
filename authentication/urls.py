from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path(route='register/', view=views.RegistrationView.as_view(), name='register'),
    path(route='validate-username/',
         view=csrf_exempt(views.UsernamevalidationView.as_view()), name='validate-username'),
]
