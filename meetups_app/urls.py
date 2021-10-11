"""meetups_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # redirect the '/' path to the '/meetups' path
    path('', RedirectView.as_view(url='/meetups')),
    # first argument act like a prefix to the urls from the include 
    path('meetups/', include('meetups.urls'))
    # we add this to tell django how to serve the uploaded files
    # these are static files that are uploaded at current time
    # media_url is the request url and media_root is the path to the actual files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops 
# off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf 
# for further processing.

# The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf 
# (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, 
# or any other path root, and the app will still work.

