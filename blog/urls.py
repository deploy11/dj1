from django.urls import path
from .views import home,detail
urlpatterns = [
    path('',home,name='blog'),
    path('post/<int:pk>/',detail.as_view(),name="details")
]
