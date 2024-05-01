from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CustomerBioList.as_view()),
    path('customerbio/<int:pk>', views.CustomerBioDetail.as_view())
]
