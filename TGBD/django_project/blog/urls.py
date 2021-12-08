from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/$', views.post_details, name='post_detail'),
    #url(r'^/time',views.today_is,name='blog_time')
   
]