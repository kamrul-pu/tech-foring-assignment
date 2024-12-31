"""Urls mappings for users."""

from django.urls import path

from core.views.user import (
    UserDetail,
    UserRegistration,
    UserLogin,
)

urlpatterns = [
    path("/<int:id>", UserDetail.as_view(), name="user-details"),
    path("/register", UserRegistration.as_view(), name="user-registration"),
    path("/login", UserLogin.as_view(), name="user-login"),
]
