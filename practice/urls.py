
from django.urls import path
from .views import create_users, create_videos,annotate, bulk_create_users

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create_users/', create_users,name="create_users"),
    path('bulk_create_users/', bulk_create_users,name="bulk_create_users"),
    path('create_videos/', create_videos,name="create_videos"),
    path('annotate/', annotate,name="annotate"),
]
