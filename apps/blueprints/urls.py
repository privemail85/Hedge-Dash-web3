from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^createablueprint', views.createablueprint, name='createablueprint'),
	url(r'^instructions', views.instructions, name='instructions'),
	url(r'^myblueprints', views.myblueprints, name='myblueprints'),
	url(r'^purchasedblueprints', views.purchasedblueprints, name='purchasedblueprints'),
	url(r'^blueprintsubmissionconfirmation', views.blueprintsubmissionconfirmation, name='blueprintsubmissionconfirmation'),
]