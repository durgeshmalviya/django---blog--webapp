from  django.urls  import  path
from .import  views


urlpatterns =[
path('', views.Bloging, name= 'Bloging'),
path('<int:pk>/', views.Bloging_detail, name='Bloging_detail'),
]