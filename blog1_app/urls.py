from django.urls import path

from blog1_app import views

urlpatterns = [
    path(
        "",
        views.PostListView.as_view(), 
        name="post1-list"),
    path(
        "post1-detail/<int:pk>/",
        views.PostDetailView.as_view(), 
        name="post1-detail"),
    path(
        "post1-delete/<int:pk>/",
        views.PostDeleteView.as_view(), 
        name="post1-delete"),
    path(
        "post1-create/",
        views.PostCreateView.as_view(), 
        name="post1-create"),
    path(
        "draft1-list/",
        views.DraftListView.as_view(), 
        name="draft1-list"),
    path(
        "post1-publish/<int:pk>/",
        views.PostPublishView.as_view(), 
        name="post1-publish"),
    path(
        "post1-update/<int:pk>/",
        views.PostUpdateView.as_view(), 
        name="post1-update"),
 ]
