from django.db import models

# Create your models here.
# Registration models
class Registration(models.Model):
	firstname = models.CharField(max_length= 30)
	lastname  = models.CharField(max_length= 30)
	location  = models.CharField(max_length= 150)
	phone     = models.IntegerField()
	email     = models.EmailField()


	class Meta:
		verbose_name='Registration'
		verbose_name_plural ='Registrations'

	def __str__(self):
		return self.firstname
# end of the Registration models

# Donations Model

class Donations(models.Model):
	fullname = models.CharField(max_length= 100)
	phone    = models.IntegerField()
	Amount   = models.IntegerField()
	mpesaCode = models.CharField(max_length= 150)


	class Meta:
		verbose_name = "Donation"
		verbose_name_plural = "Donations"


	def __str__(self):
		return self.fullname
# end of the Donations Model

# Upcoming events model		

class UpcomingEvent(models.Model):
	theme         = models.CharField(max_length=200)
	img           = models.ImageField(upload_to = 'pics')
	description   = models.TextField(default='Coming soon')
	day_of_event  = models.DateField()
	venue         = models.CharField(max_length= 100)
	time_of_event = models.CharField(max_length= 50)

	class Meta:
		verbose_name = 'UpcomingEvent'
		verbose_name_plural = 'UpcomingEvents'

	def __str__(self):
		return self.theme
#end of the Upcoming events model

# Newletter subscription

class NewsletterSubscription(models.Model):
	email = models.EmailField()
	subsrciption_date = models.DateField(auto_now_add=True)


	class Meta:
		verbose_name = "NewsletterSubscription"
		verbose_name_plural = "NewsletterSubscriptions"

	def __str__(self):
		return self.email

# end of the Newletter subscription

# Testmony Model
class Testimony(models.Model):
	name  = models.CharField(max_length= 100)
	position = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'testimonyPics')
	testimony = models.TextField()

	class Meta:
		verbose_name='Testimony'
		verbose_name_plural = 'Testimonies'

	def __str__(self):
		return self.name
		
# end of the Testmony Model	

# PrayerItem models

class PrayerItem(models.Model):
	fullname = models.CharField(max_length= 100);
	phone    = models.IntegerField()
	message  = models.TextField()

	class Meta:
		verbose_name='PrayerItem'
		verbose_name_plural = 'PrayerItems'

	def __str__(self):
		return self.fullname
		


# end of the prayer items models	        
		        
class Sermons(models.Model):
	topic    = models.CharField(max_length=100)
	img      = models.ImageField(upload_to = 'sermonpics')
	category = models.CharField(max_length= 200)
	minister = models.CharField(max_length= 50)
	date     = models.DateField()
	link     = models.CharField(max_length=1000)

	class Meta:
		verbose_name_plural = "Sermons"

	def __str__(self):
		return self.minister
		

		
		    
		
		    
		    
		    		


		
		







