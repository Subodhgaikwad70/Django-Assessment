from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import ServiceRequestForm, SignUpForm, TrackServiceForm
from .models import ServiceRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            messages.success(request, f'Service request submitted successfully. Your request ID is {service_request.id}.') 
            return render(request, 'service_request_submitted.html', {'request_id': service_request.id})
        else:
            messages.error(request, 'Form submission failed. Please correct the errors.')
    else:
        form = ServiceRequestForm()
    
    return render(request, 'submit_service_request.html', {'form': form})



def track_service_request(request, request_id=None):
    service_details = None
    message = None

    if request.method == 'POST':
        form = TrackServiceForm(request.POST)
        if form.is_valid():
            request_id = form.cleaned_data['request_id']
            service_details, message = get_service_details(request_id)
    else:
        form = TrackServiceForm(initial={'request_id': request_id})

    return render(request, 'track_service_request.html', {'form': form, 'service_details': service_details, 'message': message})

def get_service_details(request_id):
    try:
        service_request = ServiceRequest.objects.get(pk=request_id)
        return service_request, None  # Return the service request object and no message
    except ServiceRequest.DoesNotExist:
        return None, 'Service Request not found'  # Return None and an error message
