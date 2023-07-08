from django.urls import path

from blog1_app import views

urlpatterns = [
    path(
        "",
        views.post1_list, 
        name="post1-list"),
    path(
        "post1-detail/<int:pk>/",
        views.post1_detail, 
        name="post1-detail"),
    path(
        "post1-delete/<int:pk>/",
        views.post1_delete, 
        name="post1-delete"),
    path(
        "post1-create/",
        views.post1_create, 
        name="post1-create"),
    path(
        "draft1-list/",
        views.draft1_list, 
        name="draft1-list"),
    path(
        "post1-publish/<int:pk>/",
        views.post1_publish, 
        name="post1-publish"),
    path(
        "post1-update/<int:pk>/",
        views.post1_update, 
        name="post1-update"),
]
