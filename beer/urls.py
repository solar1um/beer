from django.urls import path
from beer.views import generation
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', generation, name='generation')
]


urlpatterns += staticfiles_urlpatterns()
