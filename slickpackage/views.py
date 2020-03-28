from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from slickpackage.models import thepackage
from slickpackage.models import packagesub
from slickpackage.models import featuredproducts
from slickpackage.models import Categories
from slickpackage.models import industryproduct
from slickpackage.models import IndCategories
from slickpackage.models import Special
from slickpackage.models import Process
from .forms import ContactForm , SnippetForm, Snippetquote
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
		template = loader.get_template('home.html')
		context = {
				'products' : featuredproducts.objects.all(),
				'steps' : Process.objects.all()
				}
		return HttpResponse(template.render(context, request))


def about(request):
		return render(request, 'about.html')

def terms(request):
		return render(request, 'terms.html')

def contact(request):

		if request.method == 'POST':
			form = ContactForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				email =  form.cleaned_data['email']

				print(name,email)


		form = ContactForm()
		return render(request, 'contact.html', {'form':form})


def snippet_detail(request):

		if request.method == 'POST':
			form = SnippetForm(request.POST)
			if form.is_valid():
				form.save()
		form = SnippetForm()
		return render(request, 'contact.html', {'form':form})


def package(request):
		template = loader.get_template('package.html')
		context = {
				'boxes' : thepackage.objects.all() 
				}
		
		return HttpResponse(template.render(context, request))

def whyus(request):
	template = loader.get_template('whyus.html')
	context = {
			'whyus' : Special.objects.all() 
			}
	return HttpResponse(template.render(context, request))

def industry(request):
	template = loader.get_template('industry.html')
	context = {
		'indus' : industryproduct.objects.all() 
	}
	return HttpResponse(template.render(context, request))

def category(request):

	template = loader.get_template('category.html')
	context = {
			'items' : Categories.objects.all() 
			}
	return HttpResponse(template.render(context, request))

# def search(request):
# 	template = loader.get_template('category.html')
# 	# queryset_list = Categories.objects.active()
# 	query = request.GET.get("q")
# 	result = Categories.objects.filter(Q(title__iconrains=query))
	
	
def industrycategory(request):
	template = loader.get_template('industrycategory.html')
	context = {
			'incat' : IndCategories.objects.all() 
			}
	return HttpResponse(template.render(context, request))


def snippet_quote(request):

	if request.method == 'POST':
		form = Snippetquote(request.POST)
		if form.is_valid():
			form.save()
	form = Snippetquote()
	return render(request, 'quote.html', {'form':form})

def iitem(request , itemid):
	template = loader.get_template('iitem.html')
	context = {
			'iitem' : industryproduct.objects.get(id=itemid) 
			}
	return HttpResponse(template.render(context, request))

def pitem(request , itemid):
	template = loader.get_template('pitem.html')
	context = {
			'pitem' : thepackage.objects.get(id=itemid) 
			}
	return HttpResponse(template.render(context, request))


def sitem(request , itemid):
	template = loader.get_template('sitem.html')
	context = {
			'sitem' : packagesub.objects.get(id=itemid) 
			}
	return HttpResponse(template.render(context, request))