"""{{ cookiecutter.project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from conquiztador.contrib.users.views import UserViewSet, ObtainAuthToken
from conquiztador.contrib.questions.views import QuestionViewSet

router = DefaultRouter()
urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),
    path("api/token/", ObtainAuthToken.as_view()),
)

if settings.DEBUG:
    import debug_toolbar  # NOQA

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
