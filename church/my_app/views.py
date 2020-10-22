from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Registration, Donations, UpcomingEvent, NewsletterSubscription, Testimony, PrayerItem,Sermons


# Create your views here.


def Index(request):
	events = UpcomingEvent.objects.all()[0]
	testimony = Testimony.objects.all()

	context = {
	   'events':events,
	   'testimony':testimony,
	}
	return render(request, 'index.html', context)


def sermons(request):
	sermons = Sermons.objects.all()
	context = {
	  'sermon':sermons,
	     }
	return render(request, 'sermons.html',context)


def contact(request):
	if request.method =='POST':
		fullname = request.POST['fname']
		phone    = request.POST['phone']
		message  = request.POST['message']

		prayer = PrayerItem.objects.create(fullname = fullname, phone = phone, message = message)
		prayer.save()
		messages.info(request, "Your Message have been sent Successfully!")

	
	return render(request, 'contact.html',)

def upcoming(request):
	events = UpcomingEvent.objects.all()
	

	return render(request, 'events.html', {'events':events})

def registration(request):
	return render(request, 'registration.html')

def aboutUs(request):
	return render(request,'about.html')






def member(request):
	if request.method == 'POST':
		firstname = request.POST['fname']
		lastname  = request.POST['lname']
		location  = request.POST['location']
		phone     = request.POST['phone']
		email     = request.POST['email']

		if Registration.objects.filter(email=email).exists():
			messages.info(request,"Email is already Registered")
			return redirect('registration')
		elif Registration.objects.filter(phone=phone).exists():	
			messages.info(request,"Phone Number already Registered")
			return redirect('registration')

		else:
		  member = Registration.objects.create(firstname=firstname,lastname=lastname,
		  	        location=location,phone=phone,email=email)
		  messages.info(request,'You have Registered Successfully')

	return redirect('registration')	  
		  	       	

def donations(request):
	if request.method =='POST':
		fullname      = request.POST['fname']
		phone         = request.POST['phone']
		Amount        = request.POST['amount']
		mpesaCode     = request.POST['code']

		donation =Donations.objects.create(fullname=fullname,phone=phone,Amount=Amount,mpesaCode=mpesaCode)
		donation.save()
		messages.info(request,'Thank you for your Donation.God Bless Your')
		return redirect('/')

	return redirect('/')



def subscription(request):
	if request.method == 'POST':
		email = request.POST['email']

		subscriber = NewsletterSubscription.objects.create(email = email)

		subscriber.save()
		messages.info(request,'You have Subscribed')
		return redirect('/')

	return redirect('/')	

	





