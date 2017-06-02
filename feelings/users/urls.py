from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^dashboard/$',views.Dashboard.as_view(), name= 'dashboard'),
    url(r'^logout/$',views.Logout_view.as_view(), name= 'logout'),
    url(r'^signup/$',views.Signup_view.as_view(), name= 'signup'),
    url('^', include('django.contrib.auth.urls')),
]