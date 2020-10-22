from django.contrib import admin
from .models import Registration, Donations, UpcomingEvent, NewsletterSubscription, Testimony, PrayerItem,Sermons

# Register your models here.

admin.site.register(Registration)
admin.site.register(Donations)
admin.site.register(UpcomingEvent)
admin.site.register(NewsletterSubscription)
admin.site.register(Testimony)
admin.site.register(PrayerItem)
admin.site.register(Sermons)
