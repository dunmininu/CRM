from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from leads.views import landing_page, LandingPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", LandingPageView.as_view(), name="landing_page"),
    path("leads/", include("leads.urls", namespace="leads")),
]
