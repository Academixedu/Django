from django.urls import path
from . import views
urlpatterns=[
 path('app/sample/', views.sample_get_view, name='sample_get_view'),
 path('app/sample1/',views.sample1,name='sample1'),
 path('app/sample2/<str:name>',views.sample2,name='sample2'),
 path('app/sample3/',views.sample3,name='sample3')
]