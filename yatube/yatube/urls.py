from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('about/', include('about.urls', namespace='about')),
    path("", include("posts.urls")),
    path('admin/my-admin/', admin.site.urls)
]
