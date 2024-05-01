from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CustomerBioList.as_view()),
    path('customerbio/<int:pk>', views.CustomerBioDetail.as_view()),
    path('purshes', views.PurchesList.as_view()),
    path('purshes/<int:pk>', views.PurchesDetail.as_view()),

]
