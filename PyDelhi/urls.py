from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("book_store.api.urls")),
    path("silk/", include("silk.urls", namespace="silk")),
]
