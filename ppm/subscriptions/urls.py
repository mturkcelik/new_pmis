from django.urls import path, include


path("stripe/", include("djstripe.urls", namespace="djstripe"))