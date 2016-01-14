from django.conf.urls import patterns, include, url
from app import views
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'AtomOA.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', views.index, name='index'),
                       url(r'^login/', views.user_login, name='user_login'),
                       url(r'^register/', views.user_register,
                           name='user_register'),
                       url(r'^logout/$', views.user_logout, name='user_logout'),
                       url(r'^userlog/$', views.userlog, name='userlog'),
                       url(r'^managlog/$', views.managlog, name='managlog'),
                       url(r'^managsend/$', views.managsend, name='managsend'),
                       url(r'^usernotice/$', views.usernotice, name='usernotice'),
                       )
