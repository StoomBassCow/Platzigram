"""Modulos URLS """
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', view=local_views.hello_world),
    path('sorted/', view=local_views.sort_integers),
    path('hi/<str:name>/<int:age>', view=local_views.say_hi),
    path('posts/', view=posts_views.list_posts),
    path('users/login/', view=users_views.login_view, )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)