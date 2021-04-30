from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("posts.urls")),
    path('admin/', admin.site.urls)
]
