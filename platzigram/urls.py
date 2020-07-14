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
    path('posts/', view=posts_views.list_posts, name='feed'),
    path('users/login/', view=users_views.login_view,  name='login'),
    path('users/logout/', view=users_views.logout_view,  name='logout'),
    path('users/signup/', view=users_views.signup_view,  name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 