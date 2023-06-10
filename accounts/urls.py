from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("signin", views.sign_in),
    path("signup", views.sign_up),
    path("signout", views.sign_out),
    path("<str:profile_username>", views.show_profile),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)