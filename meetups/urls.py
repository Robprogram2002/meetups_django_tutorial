from django.urls import path
from . import views

# the name is mandatory since django would be searching for a varibale with that name in this file
urlpatterns = [
  # we specify the url path, then the view (the callback function) that would be call and finally the unique name
  path('greetings/', views.home_greeting, name='greeting'),    
  path('', views.index, name='all-meetups'), # our-domain.com/meetups
  path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
  path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]

# The next step is to point the root URLconf at the polls.urls module

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name

# route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in 
# urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one 
# that matches.
# Patterns don’t search GET and POST parameters, or the domain name. 

# When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first 
# argument and any “captured” values from the route as keyword arguments

# Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. 
# This powerful feature allows you to make global changes to the URL patterns of your project while only touching 
# a single file.

