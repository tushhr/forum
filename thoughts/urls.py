from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.show_post),
    path("<int:id>/comment", views.write_comment),
    path("delete/post/<int:id>", views.delete_post),
    path("post", views.create_post),
]