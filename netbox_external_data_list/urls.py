from django.urls import path
from .views import ExternalDataListView


urlpatterns = [
    # The value in the "name" argument is used in menu item in navigation.py
    path("datalist/", ExternalDataListView.as_view(), name="datalist"),
]
