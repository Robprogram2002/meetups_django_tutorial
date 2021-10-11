from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegistrationForm
from . models import Meetup
 
# Create your views here.

# A view is just a python pure function that take special argumentents and that is callback
# To call the view, we need to map it to a URL - and for this we need a URLconf.
def home_greeting(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    meetups = Meetup.objects.all()

    # the second argument of render function is the path (relative to the templates folder) to the template file
    # taht would be render.
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })

# we need to specify the second argument when in the url path a variable is specified
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'owner_email': meetup.owner_email
    })