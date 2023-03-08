from django.urls import path, include


urlpatterns = [
    path("stripe/", include("djstripe.urls", namespace="djstripe"))
]