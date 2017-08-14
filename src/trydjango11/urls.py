"""trydjango11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from game import views as game_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', game_view.home, name="home"),
    url(r'^car/$', game_view.car, name="car"),
    url(r'^piano/$', game_view.piano, name="piano"),
    url(r'^plant/$', game_view.plant, name="plant"),
    url(r'^country/$', game_view.country, name="country"),
    url(r'^country/london$', game_view.london, name="london"),
    url(r'^country/sarawak$', game_view.sarawak, name="sarawak"),
    url(r'^cartoon/$', game_view.cartoon, name="cartoon"),
    url(r'^cartoon/videop$', game_view.videop, name="videop"),
    url(r'^cartoon/videof$', game_view.videof, name="videof"),
    url(r'^cartoon/videos$', game_view.videos, name="videos"),
    url(r'^preguess$', game_view.preguess, name="preguess"),
    url(r'^guess$', game_view.guess, name="guess"),
    url(r'^pregift$', game_view.pregift, name="pregift"),
    url(r'^gift$', game_view.gift, name="gift"),

]

# car
# piano
# plant
# cartoon
# country


