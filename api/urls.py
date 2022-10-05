from django.urls import path

from . import views

urlpatterns = [
    path('studentapi/',views.hello_word, name="hello_word"),
]
