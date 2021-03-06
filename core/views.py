from django.shortcuts import render, redirect
from django.contrib.auth.models import User as authUser
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event, User
from datetime import datetime
from . import mybarcode
import random
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import viewsets
from .serializers import UserSerializer, EventSerializer

# Create your views here.

def homeview(request):
	if not request.user.is_authenticated:
		return redirect('login_user')
	else:
		return redirect('dashboard')

def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			return redirect('login_user')
	else:
		context = {}
		if request.user.is_authenticated:
			return redirect('dashboard')
		else:
			return render(request, 'core/login_form.html', context)	

@login_required(login_url='/login/')
def logout_user(request):
	logout(request)
	return redirect('login_user')

@login_required(login_url='/login/')
def dashboard(request):
	context = {
		'events' : Event.objects.all(),
	}
	return render(request, 'core/show_events.html', context)

@login_required(login_url="/login/")
def create(request):
	if request.method=="POST":
		name = request.POST.get("name")
		description = request.POST.get("description") 
		price = request.POST.get("price")
		organized_by = request.POST.get("organizer")
		date = request.POST.get("date")
		time = request.POST.get("time")
		image = request.FILES["image"]
		location = request.POST.get("location")

		temp = Event.objects.create(name=name, description=description, price=price, organized_by=organized_by, date=date, time=time, picture=image, location=location)
		barcode_file_name = 'barcode_event_' + str(temp.id)
		unique_code = random.randint(9000000,100000000)
		barcode = mybarcode.MyBarcodeDrawing(unique_code).save(formats=['gif'],outDir='media/barcodes',fnRoot=barcode_file_name)
		barcode = barcode.replace('media/', "")
		temp.barcode = barcode
		temp.unique_code = unique_code
		temp.save()

		return redirect('dashboard')
	else:
		context = {}
		return render(request, 'core/create_event.html', context)

@login_required(login_url="/login/")
def delete_event(request, event_id):
	temp = Event.objects.get(id=event_id)
	temp.delete()

	return redirect('dashboard')

@login_required(login_url="/login/")
def update_event(request, event_id):
	if request.method=="POST":
		name = request.POST.get("name")
		description = request.POST.get("description") 
		price = request.POST.get("price")
		organized_by = request.POST.get("organizer")
		date = request.POST.get("date")
		time = request.POST.get("time")
		image = request.FILES["image"]
		location = request.POST.get("location")
		print(request.FILES)
		temp = Event.objects.get(id=event_id)

		if image is not None:
			temp.picture = image

		temp.name = name 
		temp.description = description 
		temp.price = price 
		temp.organized_by = organized_by 
		temp.date = date 
		temp.time = time 
		temp.location = location 
		temp.save()

		return redirect('dashboard')
	else:
		context = {
			'event': Event.objects.get(id=event_id),
			'datetime': datetime.now().date,
		}
		return render(request, 'core/event_update.html', context)

@login_required(login_url="/login/")
def send_email(request, event_id):

	context = {
		'event': Event.objects.get(id=event_id),
		'datetime': datetime.now().date,
	}

	subject = "Invitation for " + Event.objects.get(id=event_id).name
	to = list()
	for user in User.objects.all():
		to.append(user.email)

	print(to)
	from_email = 'raazu889@gmail.com'

	html_content = render_to_string('core/email.html', context) # render with dynamic value
	text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

	# create the email, and attach the HTML version as well.
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

	return render(request, 'core/email.html', context)

@login_required(login_url="/login/")
def user_add(request):
	if request.method=="POST":
		name = request.POST.get('name') 
		email = request.POST.get('email')
		phone = request.POST.get('phone')

		temp = User.objects.create(name=name, email=email, phone=phone)
		temp.save
		messages.add_message(request, messages.INFO, "Successfully Added User")
		return redirect('show_users')
	else:
		context = {}
		return render(request, 'core/user_add.html', context)

@login_required(login_url="/login/")
def show_users(request):
	context = {
		'users' : User.objects.all(),
	}
	return render(request, 'core/user_show.html', context)

@login_required(login_url="/login/")
def user_delete(request, user_id):
	temp = User.objects.get(id=user_id)
	temp.delete()
	messages.add_message(request, messages.INFO, "Successfully Deleted User")
	return redirect('show_users')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
