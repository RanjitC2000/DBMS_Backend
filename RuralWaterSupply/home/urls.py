from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('status/',views.status,name='status'),
    path('apply/',views.apply,name='apply'),
    path('healthscheme/', views.healthscheme,name='healthscheme'),
    path('community/',views.community,name='community'),
    path('status/requestpost',views.requestpost,name='requestpost'),
]
