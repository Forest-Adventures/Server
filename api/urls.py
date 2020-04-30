from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.authtoken import views
from notes.api import PersonalNoteViewSet
from accounts.serializers import UserViewSet

router = routers.DefaultRouter()
router.register(r'notes', PersonalNoteViewSet)
##make route for login and register use something different the PersonalNoteVewSet.
router.register(r'register', UserViewSet, 'register')

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('api/', include(router.urls)),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
]
