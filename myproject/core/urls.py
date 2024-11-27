from django.urls import path
from . import views
urlpatterns=[
 path('app/sample/', views.sample_get_view, name='sample_get_view'),
 path('app/sample1/',views.sample1,name='sample1'),
 path('app/sample_text_view/', views.sample_text_view, name= 'sample_text_view'),
 path('app/new/', views.new, name= 'new'),
]