from django.urls import path
from django.conf.urls import url;
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('status/',views.status,name='status'),
    path('apply/',views.apply,name='apply'),
    path('healthscheme/', views.healthscheme,name='healthscheme'),
    path('community/',views.community,name='community'),
    path('status/requestpost',views.requestpost,name='requestpost'),
    path('apply/save',views.save,name='save'),
    url(r'^(?P<slug>[\w-]+)/$',views.community_detail,name='detail'),
    path('community/messages',views.Commessage,name='commessage'),
    path('community/SendMessage',views.SendMessage,name='send'),
]
