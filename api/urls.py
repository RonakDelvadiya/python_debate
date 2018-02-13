from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from rest_framework.authtoken import views as tokenView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^list/$',discussions_list),
    url(r'^create/$',comment_create),
    url(r'^details/list/$', DiscussionListSearch),
    url(r'^details/list/all/$', DiscussionListSearchAll),
    url(r'^typelist/$',Disc_type_list.as_view()),
    url(r'^searchall/$',Disc_search_by_title_text_disctype.as_view()),
    url(r'^searchtitle/$',Get_search_Disc_title.as_view()),
    url(r'^create/$', Create_comment.as_view()),
]