from django.shortcuts import render,redirect
from newapp.models import Shop
from newapp.forms import ShopForm
def read(request):
	shop=Shop.objects.all()
	return render(request,'apps/result.html',{'s':shop})
def insert(request):
	form=ShopForm()
	if request.method=="POST":
		form=ShopForm(request.POST)
		if form.is_valid():
			form.save()	
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	s=Shop.objects.get(id=id)
	s.delete()
	return redirect('/result')
def update(request,id):
	shop=Shop.objects.get(id=id)
	if request.method=="POST":
		form=ShopForm(request.POST, instance=shop)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'s':shop})
def index(request):
    return render(request,'apps/index.html')
def shop(request):
    return render(request,'apps/shop.html')
def men(request):
    return render(request,'apps/men.html')
def women(request):
    return render(request,'apps/women.html')
def Beauty(request):
    return render(request,'apps/beauty.html')
def footwear(request):
    return render(request,'apps/footwear.html')
def zworld(request):
    return render(request,'apps/z-world.html')
def kids(request):
    return render(request,'apps/kids.html')
def contact(request):
    return render(request,'apps/contact.html')

