from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name= 'about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_question/$', views.add_question, name = 'add_question'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'), 
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
)
