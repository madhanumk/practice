from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Video
from django.db.models import Avg, Count, Max

# Create your views here.


def create_users(request):
    for i in range(0,100):
        user=User.objects.create_user('foo'+str(i), password='bar')


    return render(request, 'user_creates.html')

def bulk_create_users(request):
    users = [User(username=f'foo{i}', password='bar') for i in range(100)]
    User.objects.bulk_create(users)


    return render(request, 'user_creates.html')


def create_videos(request):
    for i in range(1,6):
        user = User.objects.all().order_by('?').first()
        user_likes = User.objects.all().order_by('?')[:5+i]
        likes_object = []
        for user_like in user_likes:
            likes_object.append(user_like)


        video=Video.objects.create(name="Sample Video "+str(i),created_by=user)
        video.user_likes.set(likes_object)


    return render(request, 'user_creates.html')


def annotate(request):
    video = Video.objects.values_list('name').aggregate(avg_likes = Avg('user_likes'),max_likes= Max('user_likes'))
    print(video)

    video = Video.objects.values('id', 'name').annotate(likes_count = Count('user_likes',distinct=True), avg_likes = Avg('user_likes')).filter(likes_count__gt=8)
    print(video)

    return render(request, 'user_creates.html')