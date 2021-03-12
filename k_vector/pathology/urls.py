from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sample/new", views.sample_form, name="sample_form"),
    path("sample/<int:sample_id>", views.sample_view, name="sample_view"),
    path("sample/<int:sample_id>/edit", views.sample_edit_view, name="sample_edit_view"),
    path("sample/<int:sample_id>/delete", views.sample_delete_view, name="sample_delete_view"),
    path("sample/list", views.samples_list, name="samples_list"),
    path("team", views.team, name="team"),
]
