from django.shortcuts import render, HttpResponseRedirect
from .models import ProductModel
from .forms import ProductModelForm

# Create your views here.
def product_home(request):
	qs = ProductModel.objects.all()
	context = {'products':qs}

	return render(request, 'index.html', context)

def product(request):
	qs = ProductModel.objects.all()
	return render(request, 'products.html', {'objects':qs})

def product_detail(request, pk):
	product = ProductModel.objects.get(id=pk)
	return render(request, 'product_details.html', {'pr':product})

def add_product(request):
	form = ProductModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		f = form.save(commit=False)
		f.save()
		return HttpResponseRedirect('/products/')

	context = {'form':form}
	return render(request, 'add_product.html', context)

def edit_product(request, pk):
	instance = ProductModel.objects.get(id=pk)
	form = ProductModelForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		f = form.save(commit=False)
		f.save()
		return HttpResponseRedirect('/products/')

	context = {'form':form, 'instance':instance}
	return render(request, 'edit_product.html', context)

def delete_product(request, pk):
	qs = ProductModel.objects.get(id=pk)
	if request.method == 'POST':
		qs.delete()
		return HttpResponseRedirect('/products/')

	return render(request, 'delete_product.html', {'product':qs})

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')