from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'personnel'

urlpatterns = [
    path('',views.home,name='home'),
    path('status/',views.status,name='status'),
    path('healthscheme/', views.healthscheme,name='healthscheme'),
    path('community/',views.community,name='community'),
    path('publish/',views.publish,name='publish'),
    path(r'^(?P<subject>[\w-]+)/$',views.community_detail,name='detail'),
    path(r'^(notice/?P<title>[\w-]+)/$',views.notice,name='notice'),
    path('community/messages/',views.Commessage,name='commessage'),
    path('bigProj/',views.bigProj,name='bigProj'),
    path('smallProj/',views.smallProj,name='smallProj'),
    path('bookappoint/',views.appointview,name='appointview'),
    path('personnelview/',views.personnel,name='personnelview'),
    path('organizationview/',views.organization,name='organizationview'),
    path('villages/',views.village,name='villages'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
