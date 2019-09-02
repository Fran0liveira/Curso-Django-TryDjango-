from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	return render(request, "home.html", {})

def contact(request, *args, **kwargs):
	return HttpResponse("<h2>Hey, what's up doc?<h2>")

def contacts(request, *args, **kwargs):
	return render(request, "contacts.html", {})

def about(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [234, 345, 456, "ABCD"]

	}
	return render(request, "about.html", my_context)