from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

from leads.views import LandingPageView, SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", LandingPageView.as_view(), name="landing_page"),
    path("leads/", include("leads.urls", namespace="leads")),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),

]