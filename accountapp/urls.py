from django.urls import path
from .views import hello
app_name = "accountapp"

urlpatterns = [
    path('', hello, name="hello")
]
