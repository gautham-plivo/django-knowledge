from django.urls import re_path

from . import views

urlpatterns = (
    re_path(r"^$", views.knowledge_index, name="knowledge_index"),
    re_path(r"^questions/$", views.knowledge_list, name="knowledge_list"),
    re_path(
        r"^questions/(?P<question_id>\d+)/$",
        views.knowledge_thread,
        name="knowledge_thread_no_slug",
    ),
    re_path(
        r"^questions/(?P<category_slug>[a-z0-9-_]+)/$",
        views.knowledge_list,
        name="knowledge_list_category",
    ),
    re_path(
        r"^questions/(?P<question_id>\d+)/(?P<slug>[a-z0-9-_]+)/$",
        views.knowledge_thread,
        name="knowledge_thread",
    ),
    re_path(
        r"^moderate/(?P<model>[a-z]+)/" r"(?P<lookup_id>\d+)/(?P<mod>[a-zA-Z0-9_]+)/$",
        views.knowledge_moderate,
        name="knowledge_moderate",
    ),
    re_path(r"^ask/$", views.knowledge_ask, name="knowledge_ask"),
)
