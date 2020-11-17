from django.urls import path
from django.conf.urls import url;
from . import views

app_name = 'home'

urlpatterns = [
    
    path('',views.home,name='home'),
    path('status/',views.status,name='status'),
    path('apply/',views.apply,name='apply'),
    path('healthscheme/', views.healthscheme,name='healthscheme'),
    path('community/',views.community,name='community'),
    path(r'^(?P<slug>[\w-]+)/$',views.community_detail,name='detail'),
    path(r'^(notice/?P<title>[\w-]+)/$',views.notice,name='notice'),
    path('community/messages/',views.Commessage,name='commessage'),
    path('bigProj/',views.bigProj,name='bigProj'),
    path('smallProj/',views.smallProj,name='smallProj'),
    path('appoint/',views.appoint,name='appointment'),
]
