from django.urls import path
from . import views
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='addexpense/', view=views.add_expense, name='add_expense')
]
