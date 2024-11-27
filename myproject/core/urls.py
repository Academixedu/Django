from django.urls import path
from . import views
urlpatterns=[
 path('app/sample/', views.sample_get_view, name='sample_get_view'),
 path('app/sample1/',views.sample1,name='sample1'),
 path('app/tharun/',views.tharun,name='tharun'),
 path('app/tharun/',views.tharun1,name='tharun1'),
]