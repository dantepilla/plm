
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers
from .views import listPlmViewset, plmProcessing




router = DefaultRouter()
# router.register('plm/executing/<str:server>/', views.listPlmViewset, basename='plm-viewset')

urlpatterns = [

    path('execution/<str:server>/<str:stage>/<str:step>/', views.plmProcessing),
    
]


