from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', LandingPageView.as_view(), name='landing_page'),
	url(r'^registration/$', UserRegistrationView.as_view(), name='registration_page'),
	url(r'^login/$', user_login, name='login'),
	url(r'^logout/$', user_logout, name='logout'),
	url(r'^home/(?P<pk>\d+)/$', view_profile, name='home'),
	url(r'^search/$', search_user, name='search'),
	url(r'^createProfile/$', UserProfileCreationView, name='createProfile'),
	url(r'^aboutus/$', AboutUs.as_view(), name='aboutus'),
	url(r'^contactus/$', ContactUs.as_view(), name='contactus'),

]
