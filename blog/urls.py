from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='home'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/add_comment/$', views.post_comment,
            name='post_comment'),
]
