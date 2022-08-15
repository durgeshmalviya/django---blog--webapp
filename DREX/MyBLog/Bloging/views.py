from django.shortcuts import render
from .models  import  tutorial


def  Bloging(request):
	Tut = tutorial.objects.all()
	context = {
	'Tut': Tut,
	}
	return  render(request, 'Bloging.html', context)

def  Bloging_detail(request,pk):
	Tut = tutorial.objects.get(pk=pk)
	context = {
	'Tut': Tut,
	}
	return  render(request, 'Blogingdetail.html', context)
